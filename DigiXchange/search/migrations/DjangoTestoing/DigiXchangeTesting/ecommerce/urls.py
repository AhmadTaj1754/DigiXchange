"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from products.views import  ProductListViewTest, product_list_view_test

from accounts.views import login_page, register_page, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from .views import (home_page, about_page, contact_page, test_page, login_page_test,
register_page_test)

urlpatterns = [

    url(r'^product_list_view_test/$', ProductListViewTest.as_view()),
    url(r'^product_list_view_test-fv/$', product_list_view_test),


    url(r'^register_page_test/$', register_page_test, name='register_page_test'),







    url(r'^login_page/$', login_page_test, name="login_page_test"),
    url(r'^test/$', test_page, name='test'),
    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page, name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', login_page, name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^register/$', register_page, name='register'),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^products/$', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





































#end
