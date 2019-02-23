
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from modelapp.models import Topic,Webpage,AccessRecord
# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)

def business(request):
    webpages_list = Webpage.objects.order_by('name')
    web_dict = {"business_records":webpages_list}
    return render(request,'modelapp/index.html',web_dict)
