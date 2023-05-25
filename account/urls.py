from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/lecturer/', views.register_lecturer, name='register_lecturer'),
    path('course-registration/', views.course_registration, name='course_registration'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('course-details/<int:course_id>/', views.course_details, name='course_details'),
    path('lecturer/<int:lecturer_id>/', views.lecturer_details, name='lecturer_details'),
    path('lecturer/dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('login/', views.login_view, name='login'),
    path('admin/', views.admin, name='admin'),
    path('lecturer/', views.lecturer, name='lecturer'),
    path('student/', views.student, name='student'),
]
