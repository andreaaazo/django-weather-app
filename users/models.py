from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class DataberryUser(AbstractUser):
    profile_image = models.ImageField(upload_to="users/", default="no_image.png")