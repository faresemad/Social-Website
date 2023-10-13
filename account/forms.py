# This file defines forms for user registration, login, profile editing, and user editing.

from django import forms
from django.contrib.auth.models import User

from .models import Profile

# This class defines a form for editing user details.
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    # This method validates the email field to ensure it's unique.
    def clean_email(self):
        data = self.cleaned_data["email"]
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError(" Email already in use.")
        return data


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )


# This class defines a form for user registration.
class UserRegistrationForm(forms.Form):
    # Password field.
    password = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )
    # Password confirmation field.
    password2 = forms.CharField(
        label="Repeat Password", max_length=100, widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    # This method validates the password confirmation field.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    # This method validates the email field to ensure it's unique.
    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already in use.")
        return data
