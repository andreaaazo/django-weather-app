from django.contrib import admin
from .models import DataberryUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.register(DataberryUser, UserAdmin)
