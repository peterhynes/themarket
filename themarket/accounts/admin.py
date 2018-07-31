from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from .models import GuestEmail
from . forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin', 'staff', 'retailer',)
    list_filter = ('admin', 'staff', 'retailer',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Account Type', {'fields': ('admin', 'staff', 'retailer', 'customer',)}),
        ('User Info', {'fields': ('name', 'address', 'business_name', 'business_address', 'rbn', 'business_type', 'active',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'admin', 'staff', 'retailer', 'customer',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin,)

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = GuestEmail

admin.site.register(GuestEmail, GuestEmailAdmin)