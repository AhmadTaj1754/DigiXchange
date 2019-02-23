
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from modelapp.models import Topic,Webpage,AccessRecord
from . import forms

# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'modelapp/index.html',date_dict)

# def business(request):
#     webpages_list = Webpage.objects.order_by('name')
#     date_dict = {"access_records":webpages_list}
#     return render(request,'modelapp/index.html',date_dict)
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'modelapp/form_page.html',{'form':form})


























#end
