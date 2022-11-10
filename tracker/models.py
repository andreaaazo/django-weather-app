from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=20)
    favourites = models.ManyToManyField(get_user_model(), default=None, blank=True)

    def __str__(self):
        return self.city