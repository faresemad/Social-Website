from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )


class UserRegistrationForm(forms.Form):
    password = forms.CharField(
        label="Password", max_length=100, widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Repeat Password", max_length=100, widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]
