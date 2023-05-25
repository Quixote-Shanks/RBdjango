from django.contrib import admin
from .models import User, Student, Lecturer, Course

class CourseInline(admin.TabularInline):
    model = Lecturer.courses.through

class LecturerAdmin(admin.ModelAdmin):
    inlines = [CourseInline]

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('lecturers',)

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Course, CourseAdmin)
