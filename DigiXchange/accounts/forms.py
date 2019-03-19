from django import forms
from django.contrib.auth import get_user_model

import re

User = get_user_model()


# secure password
def valid_password(password):
    valid=False
    digit=re.findall("\d", password)
    if not digit:
        raise forms.ValidationError("Passwords must have at least one digit.")
    special=re.findall("[!@#$%^&*-]", password)
    if not special:
        raise forms.ValidationError("Passwords must have at least one of the following special characters: !@#$%^&*")
    passlength= len(password) > 10
    print(passlength)
    if not passlength:
        raise forms.ValidationError("Passwords must have at 10 or more characters.")
    valid=True
    return valid

class GuestForm(forms.Form):
    email    = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=
        {"class":"form-control"}
        ))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
        {"class":"form-control"}
    ))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=
        {"class":"form-control"}
        ))
    email    = forms.EmailField(widget=forms.EmailInput(attrs=
        {"class":"form-control"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
        {"class":"form-control"}
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs=
        {"class":"form-control"}
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        if valid_password(password):
            return data














































# endbl
