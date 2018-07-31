from django.urls import path, re_path

from . views import (
        RetailerSignUpView,
        CustomerSignUpView,
        guest_register_view,
        AccountHomeView,
        )


app_name = 'accounts'
urlpatterns = [
    path("", guest_register_view, name='guest_register'),
    path("signup/retailer/", RetailerSignUpView.as_view(), name='retailer_signup'),
    path("signup/customer/", CustomerSignUpView.as_view(), name='customer_signup'),
    path("myaccount/", AccountHomeView.as_view(), name='account_home'),
]