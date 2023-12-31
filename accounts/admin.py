from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields':('image',)}),
    )# admindagi userlar ro'yxatida image chiqishi uchun fieldsdagi fieldlar ro'yxatiga 'image' qo'shildi.
    list_display = [
        "id",
        "email",
        "username",
        "is_superuser",
        "is_staff",
        "image"
    ]  

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)