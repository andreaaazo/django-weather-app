from django.shortcuts import render
from django.views import View

from api.get_current_weather import get_current_weather

# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):

        dubai = get_current_weather("Dubai")
        new_york = get_current_weather("New York")
        london = get_current_weather("London")
        tokyo = get_current_weather("Tokyo")

        context = {
            "dubai": dubai,
            "new_york": new_york,
            "london": london,
            "tokyo": tokyo,
        }

        return render(request, "home.html", context)
