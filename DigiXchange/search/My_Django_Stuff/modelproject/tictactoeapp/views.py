from django.shortcuts import render
from django.http import HttpResponse
from modelapp.models import Topic,Webpage,AccessRecord

# Create your views here.
def tictactoe(request):

    return render(request,'tictactoeapp/tictactoe.html')
