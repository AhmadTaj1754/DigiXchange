from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<strong>Ahmad Taj is doing this</strong")

def index(request):
    my_dict = {'insert_me':"Now I am coming from index.html!"}
    return render(request,'secoundapp/index.html',context=my_dict)


# def help(request):
#     help_dic={'insert_here': 'We are here to help !'}
#     return render(request,'secoundapp/help.html',context=help_dic)
#
#Create your views here.
