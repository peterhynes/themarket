from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm

def home_page(request):
    context = {
        "title":"Home page",
        "content":"welcome to the home page",
    }
    if request.user.is_authenticated:
        context["logged_in_content"] = "Logged in content"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":"welcome to the about page"
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm()
    context = {
        "title":"Contact Page",
        "content":"welcome to the contact page",
        "form": contact_form,
    }
    return render(request, "contact/view.html", context)

