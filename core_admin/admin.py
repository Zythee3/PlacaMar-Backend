from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin

@admin.register(Admin)
class AdminAdmin(UserAdmin):
    model = Admin
    list_display = ('username', 'email', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets