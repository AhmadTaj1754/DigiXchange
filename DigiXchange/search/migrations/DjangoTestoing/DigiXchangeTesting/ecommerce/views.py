from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import *


def test_page(request):
    form= TestForm(request.POST or None)
    context= {

        "title":"Boston",
        "content":"Planning phase has begun",
        "form":form,
        # "year": year,
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "test/home_page_alt.html", context)

def register_page_test(request):
    form = RegisterForm(request.POST or None)
    context={

        "title":"Register",
        "content":"Please enter pertinent information to register",
        "form":form,
    }
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "test/register.html", context)


def login_page_test(request):
    form = LoginForm(request.POST or None)
    context= {
        "title":"Login",
        "form":form,
    }
    if form.is_valid():
        print(form.cleaned_data)

        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.is_authenticated)
            # redirect("login.html")
            context['form']= LoginForm()
        else:
            print("ValidationError")

    return render(request, "test/home_page_alt.html", context)































































def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title":"DigiXchange",
        "content":"Graphic design meets engineering",

    }
    if request.user.is_authenticated():
        context["premium_content"] = "Welome, you are now login"
    return render(request, "home_page.html", context)





def about_page(request):
    context = {
        "title":"About Page",
        "content":" DigiXchange is a place where Graphic Designers and engineering meets. Find variety of widget to user withing your software engineering project."
    }
    return render(request, "home_page.html", context)




def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
