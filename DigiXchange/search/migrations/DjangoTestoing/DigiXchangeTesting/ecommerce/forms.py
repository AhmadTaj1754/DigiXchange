from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()




class TestForm(forms.Form):
        first_name= forms.CharField(
            widget= forms.TextInput(
                attrs={

                "class":"form-control",
                "placeholder":"first name",
                "id":"first_name",
                }

            )
        )

        last_name= forms.CharField(
            widget= forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder":"last name",
                }
            )
        )


        email= forms.EmailField(
            widget= forms.EmailInput(
                attrs= {
                    "class":"form-control",
                    "placeholder":"example@email.com",
                }
            )
        )

        content= forms.CharField(
            widget= forms.Textarea(
                attrs= {
                    "class":"form-control",
                    "placeholder":"enter message here",
                }
            )
        )

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if not "yahoo" in email:
                raise forms.ValidationError("Please enter an email address")
            return email



class RegisterForm(forms.Form):
    first= forms.CharField(
        widget= forms.TextInput(
            attrs= {
                "class":"form-control",
                "placeholder":"first name",
            }
        )
    )

    last= forms.CharField(
        widget= forms.TextInput(
            attrs= {
                "class":"form-control",
                "placeholder":"last name",
            }
        )
    )

    username= forms.CharField(
        widget= forms.TextInput(
            attrs= {
                "class":"form-control",
                "placeholder":"username",
            }
        )
    )

    email= forms.EmailField(
        widget=  forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"example@email.com",
            }
        )
    )


class LoginForm(forms.Form):
    username= forms.CharField(
        widget= forms.TextInput(
            attrs= {
                "class":"form-control",
                "placeholder":"username",
            }
        )
    )

    password= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class":"form-control",
                "placeholder":"password",
            }
        )
    )























































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
