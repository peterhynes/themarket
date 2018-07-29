from django.urls import path, re_path

from . views import (
        #search_list_view,
        SearchProductView,
        )


app_name = 'search'
urlpatterns = [
    path("", SearchProductView.as_view(), name='query'),
]
