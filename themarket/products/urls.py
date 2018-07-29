from django.urls import path, re_path

from . views import (
        product_list_view,
        #product_detail_view,
        product_detail_slug_view
        )


app_name = 'products'
urlpatterns = [
    path("", product_list_view, name='list'),
    #re_path(r'^(?P<pk>\d+)/?$', product_detail_view),
    re_path(r'^(?P<slug>\w+)/?$', product_detail_slug_view, name='detail'),
]
