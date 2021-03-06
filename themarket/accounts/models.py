from django.db import models
from products.models import Product
#from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, is_retailer=False, is_customer=False):
        if not email:
            raise ValueError("Please enter email address")
        if not password:
            raise ValueError("users must have a password")
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.retailer = is_retailer
        user_obj.customer = is_customer
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_retaileruser(self, name, address, business_name, business_address, rbn, business_type):
        user = self.create_user(email, password=password, is_retailer=True)
        return user

    def create_customeruser(self, name, address, business_name, business_address, rbn, business_type):
        user = self.create_user(email, password=password, is_customer=True)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True, is_admin=True)
        return user

class User(AbstractBaseUser):
    #user_products = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    retailer = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    business_name = models.CharField(max_length=255, null=True)
    business_address = models.CharField(max_length=255, null=True)
    rbn = models.IntegerField(null=True)
    business_type = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #schema_name = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_business_name(self):
        return self.business_name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_retailer(self):
        return self.retailer

    @property
    def is_customer(self):
        return self.customer

# class Domain(DomainMixin):
#     pass


class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email