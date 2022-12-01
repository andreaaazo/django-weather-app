from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class FavouriteCity(models.Model):
    city = models.CharField(max_length=30, primary_key=True)
    favourite = models.ManyToManyField(get_user_model(), default=None, blank=None)

    def __str__(self) -> str:
        return self.city
