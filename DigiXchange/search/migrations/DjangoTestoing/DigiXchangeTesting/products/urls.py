from django.conf.urls import url

from .views import (
        ProductListView,
        ProductDetailSlugView,
        ProductListViewTest,
        product_list_view_test,

        )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),

    url(r'^product_test/$', ProductListViewTest.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^produc_view/$', product_list_view_test, name='resttest'),
]
