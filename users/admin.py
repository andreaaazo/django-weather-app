from django.contrib import admin
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin

from .forms import DataberryUserChangeForm, DataberryUserCreationForm

CurrentUser = get_user_model()

# Register your models here.
class CustomDataberryUserAdmin(UserAdmin):
    add_form = DataberryUserCreationForm
    form = DataberryUserChangeForm
    model = CurrentUser

    list_display = ["email", "username", "is_staff", "profile_image"]


admin.site.register(CurrentUser, CustomDataberryUserAdmin)
