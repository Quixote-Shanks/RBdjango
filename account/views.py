from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, LecturerRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Lecturer
from .models import Student, Course
from django.db import models


def index(request):
    return render(request, 'index.html')

def register_student(request):
    msg = None
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True  # Set user as a student
            user.save()
            student = form.save(commit=False)
            student.user = user
            student.save()
            msg = 'Student registration successful'
            return redirect('login')
        else:
            msg = 'Invalid form data'
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form, 'msg': msg})

def register_lecturer(request):
    msg = None
    if request.method == 'POST':
        form = LecturerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_lecturer = True  # Set user as a lecturer
            user.save()
            lecturer = form.save(commit=False)
            lecturer.user = user
            lecturer.save()
            msg = 'Lecturer registration successful'
            return redirect('login')
        else:
            msg = 'Invalid form data'
    else:
        form = LecturerRegistrationForm()
    return render(request, 'register_lecturer.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('admin')
                elif user.is_lecturer:
                    return redirect('lecturer_dashboard')
                elif user.is_student:
                    return redirect('student')
                else:
                    msg = 'Invalid user type'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request, 'admin.html')

def lecturer(request):
    return render(request, 'lecturer.html')

def student(request):
    return render(request, 'student.html')




from django.shortcuts import render, redirect
from .models import Student, Course

def course_registration(request):
    if request.method == "POST":
        user_id = None
        username = None
        if request.user.is_authenticated:
            user_id = request.user.id
            username = request.user.username
        
        department_names = []
        course_ids = [] 
        course_names = []
        theoretical_hours = []
        practical_hours = []
        akts = []
        credits = []
        course_types = []
        branches = []
        is_course_chosen = []
        course_years = []
        
        for x in range(0, 32):
            department_names.insert(x, request.POST.get(f"department_name{x}"))
            course_ids.insert(x, request.POST.get(f"course_id{x}"))
            course_names.insert(x, request.POST.get(f"course_name{x}"))
            theoretical_hours.insert(x, request.POST.get(f"theoretical_hour{x}"))
            practical_hours.insert(x, request.POST.get(f"practical_hour{x}"))
            akts.insert(x, request.POST.get(f"akts{x}"))
            credits.insert(x, request.POST.get(f"credit{x}"))
            course_types.insert(x, request.POST.get(f"course_type{x}"))
            branches.insert(x, request.POST.get(f"branch{x}"))
            is_course_chosen.insert(x, request.POST.get(f"is_course_chosen{x}"))

            if x < 7:
                course_years.insert(x, "1.Year")
            elif 6 < x < 12:
                course_years.insert(x, "2.Year")
            elif 11 < x < 17:
                course_years.insert(x, "3.Year")
            else:
                course_years.insert(x, "4.Year")
                
            if is_course_chosen[x] == "on" and branches[x] == "Select":
                # Ders seçilmiş, fakat şube seçilmemişse hata versin.
                return redirect('course_registration')

        student, created = Student.objects.get_or_create(user_id=user_id, defaults={'user': request.user})
        if created:
            for x in range(0, 32):
                if is_course_chosen[x] == 'on':
                    is_course_chosen[x] = True
                else:
                    is_course_chosen[x] = False

                if is_course_chosen[x]:
                    course = Course.objects.create(
                        course_year=course_years[x],
                        department_name=department_names[x],
                        course_id=course_ids[x],
                        course_name=course_names[x],
                        theoretical_hour=theoretical_hours[x],
                        practical_hour=practical_hours[x],
                        akts=akts[x],
                        credit=credits[x],
                        course_type=course_types[x],
                        branch=branches[x],
                        is_course_chosen=is_course_chosen[x]
                    )
                    student.courses.add(course)
            return redirect('registration_success')
        else:
            # The student has already registered for the course
            return redirect('schedule')  # Modify the redirect URL as per your needs

    return render(request, 'course_registration.html')


def registration_success(request):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    
    student = Student.objects.get(user_id=user_id)
    registered_courses = student.courses.all()
    
    return render(request, 'registration_success.html', {'registered_courses': registered_courses})


def lecturer_details(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    courses = lecturer.courses.all().annotate(registered_students=models.Count('students'))
    return render(request, 'lecturer_details.html', {'lecturer': lecturer, 'courses': courses})

def lecturer_dashboard(request):
    lecturer = Lecturer.objects.get(user=request.user)
    courses = lecturer.courses.all()
    return render(request, 'lecturer_dashboard.html', {'courses': courses})


def course_details(request, course_id):
    lecturer = get_object_or_404(Lecturer, user=request.user)
    course = get_object_or_404(lecturer.courses, id=course_id)
    registered_students = course.students.count()
    return render(request, 'course_details.html', {'course': course, 'registered_students': registered_students})