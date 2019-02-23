from django.conf.urls import url
from modleformapp import views

app_name = 'modleformapp'

urlpatterns = [
    url(r'^users/$',views.users,name='users'),

]
