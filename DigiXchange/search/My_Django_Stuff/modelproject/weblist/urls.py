from django.conf.urls import url
from weblist import views

urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^$', views.business,name='business'),
]
