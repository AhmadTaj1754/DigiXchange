from django.shortcuts import render
# from django.http import HttpResponse
# from appTwo.models import User
from modleformapp.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'modleFormApp/index.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'modleFormApp/users.html',{'form':form})








































#end
