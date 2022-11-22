from django.urls import path
from .views import response

urlpatterns = [
    path("", response, name="tracker"),
]
