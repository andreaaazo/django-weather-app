from django.urls import path
from .views import TrackerPageView

urlpatterns = [path("", TrackerPageView.as_view(), name="tracker")]
