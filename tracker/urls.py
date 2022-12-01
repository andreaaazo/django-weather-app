from django.urls import path
from .views import TrackerPageView, TrackerAddFavourite, TrackerRemoveFavourite

urlpatterns = [
    path("", TrackerPageView.as_view(), name="tracker"),
    path("add/<str:city>", TrackerAddFavourite.as_view(), name="add_to_favourites"),
    path(
        "remove/<str:city>",
        TrackerRemoveFavourite,
        name="remove_to_favourites",
    ),
]
