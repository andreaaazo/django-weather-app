from django.urls import path

from django.contrib.auth.decorators import login_required

from .views import TrackerPageView, TrackerAddFavourite, TrackerRemoveFavourite


urlpatterns = [
    path("", TrackerPageView.as_view(), name="tracker"),
    path(
        "add/<str:city>",
        login_required(TrackerAddFavourite.as_view()),
        name="add_to_favourites",
    ),
    path(
        "remove/<str:city>",
        login_required(TrackerRemoveFavourite.as_view()),
        name="remove_to_favourites",
    ),
]
