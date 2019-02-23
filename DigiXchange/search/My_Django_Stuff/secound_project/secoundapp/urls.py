from django.conf.urls import url
from secoundapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
