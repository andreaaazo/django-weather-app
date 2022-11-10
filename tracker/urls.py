from django.urls import path
from .views import tracker_view, add_to_favorites, remove_to_favorites

urlpatterns = [
    path("", tracker_view, name="tracker"),
    path("add/<str:city>", add_to_favorites, name="add_to_favourites"),
    path("remove/<str:city>", remove_to_favorites, name="remove_to_favourites"),
]
