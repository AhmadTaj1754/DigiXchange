from django.conf.urls import url
from tictactoeapp import views

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^$', views.tictactoe,name='business'),
]
