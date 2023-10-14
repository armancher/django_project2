from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserRegisterForm

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'personnel_number')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'personnel_number')

    readonly_fields = ('personnel_number',)
    fieldsets=(
        ('Additional Info', {'fields': ('personnel_number', 'phone_number')}),
    )
        
    
   
  



