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


class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your full name"
                    }
                    )
            )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your email"
                    }
                    )
            )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message"
                    }
                )
            )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email



class EncryptForm(forms.Form):
    filepath = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "enter fill path"
                    }
                    )
            )

    password = forms.CharField(widget=forms.PasswordInput)
    passwordconfrim = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        passwordconfrim = self.cleaned_data.get('passwordconfrim')
        if passwordconfrim != password:
            raise forms.ValidationError("Passwords do not match.")
        if valid_password(password):
            return data

class DecryptForm(forms.Form):
    path = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "enter fill path"
                    }
                    )
            )

    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        return data




























# endbl
