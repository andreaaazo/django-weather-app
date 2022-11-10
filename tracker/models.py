from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class FavoriteCity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    favorite_city = models.CharField(max_length=20)

    def __str__(self):
        return self.favorite_city