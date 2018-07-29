from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from products.models import Product

class SearchProductView(ListView):
    template_name = "search/search_list_view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.none()
