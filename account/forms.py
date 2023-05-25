from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import  User, Student, Lecturer

class StudentRegistrationForm(UserCreationForm):
    matriculation_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )
    other_biodata_fields = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "matriculation_number", "full_name", "contact_number", "email", "other_biodata_fields")

class LecturerRegistrationForm(UserCreationForm):
    employee_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"}
        )
    )
    other_biodata_fields = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "employee_number", "full_name", "contact_number", "email", "other_biodata_fields")

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )
