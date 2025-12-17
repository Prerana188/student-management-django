from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Student


class StudentRegistrationForm(UserCreationForm):
    name = forms.CharField(label="Full Name", max_length=150)
    email = forms.EmailField(label="Email Address")
    phone_number = forms.CharField(label="Phone Number", max_length=15)

    class Meta:
        model = Student
        fields = ("username", "name", "email", "phone_number", "password1", "password2")

    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["name"]
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user


class StudentLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email Address")

    def clean(self):
        # Allow login via email instead of username
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if email and password:
            try:
                user = Student.objects.get(email=email)
                self.cleaned_data["username"] = user.username
            except Student.DoesNotExist:
                pass
        return super().clean()

