from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from carts.models import Cart

from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list_view.html", context)
    


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = get_object_or_404(Product, pk=pk)
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product does not exist")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product does not exist")
    context = {
        'object': instance
    }
    return render(request, "products/product_detail_view.html", context)


def product_featured_list_view(request):
    queryset = Product.objects.featured()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_featured_list_view.html", context)


def product_featured_view(request, pk=None, featured=True, *args, **kwargs):
    # instance = get_object_or_404(pk=pk, featured=True)
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product does not exist")
    instance = Product.objects.get(pk=pk, featured=True)
    if instance is None:
        raise Http404("Product does not exist")
    context = {
        'object': instance
    }
    return render(request, "products/product_featured_view.html", context)

slug = "slugged-item"
def product_detail_slug_view(request, pk=None, slug=slug, *args, **kwargs):
    try:
        instance = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404("Not found")
    except Product.MultipleObjectsReturned:
        qs = Product.objects.filter(slug=slug)
        instance = qs.first()
    except:
        raise Http404("Product does not exist")
    context = {
        'object': instance
    }
    return render(request, "products/product_detail_view.html", context)


def get_context_data(self, *args, **kwargs):
    context = super(product_detail_slug_view, self).get_context_data(*args, **kwargs)
    cart_obj, new_obj = Cart.objects.new_or_get(self.request)
    context['cart'] = cart_obj
    return context