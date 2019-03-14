#! /usr/bin/env python3

from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.views import View

from .forms import ContactForm
from .forms import EncryptForm
from .forms import DecryptForm



import pyAesCrypt, sys, os

#home page

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







def encrypt(request):
    encrypt_form = EncryptForm(request.POST or None)
    path=""
    password=""
    if encrypt_form.is_valid():
        print(encrypt_form.cleaned_data)
        if request.method == "POST":
             print(request.POST.get('filepath'))
             path= request.POST.get('filepath')
             password  = request.POST.get('password')
             print(request.POST.get('password'))


    context={
    "title":"Encrypt",
    "form": encrypt_form}


    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024

    try:
    # Encrypt
        pyAesCrypt.encryptFile(path , path+".aes" , password, bufferSize)

    except Exception as e:
        return render(request, "contact/encrypt.html", context)

    os.system('rm ' + path)



    return render(request, "contact/encrypt.html", context)




def decrypt(request):
    decrypt_form = DecryptForm(request.POST or None)
    filepath="/users/ahmadtaj"
    password=""
    if decrypt_form.is_valid():
        print(decrypt_form.cleaned_data)
        if request.method == "POST":
            filepath = request.POST.get('path')
            password = request.POST.get('password')
            print(request.POST.get('path'))

    context={
    "title":"Decrypt",
    "form":decrypt_form}

    bufferSize = 64 * 1024

    pathlen = len(filepath)
    print(pathlen)

    endrange = pathlen - 3


    print(filepath)
    pathwithout, empty = os.path.splitext(filepath)[0:endrange]
    print(pathwithout)

# fileWithout, empty =  os.path.splitext(filePathDecrypt)[0:endRange]
    try:
        pyAesCrypt.decryptFile(filepath, pathwithout, password, bufferSize)
    except Exception as e:
        return render(request, "contact/decrypt.html", context)



    removeFile= filepath

    os.system('rm ' + removeFile)

    return render(request, "contact/decrypt.html", context)












































# end
