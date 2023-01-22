from django.shortcuts import render
from django.views import View

from api.weather_prevision import get_current_weather

# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):

        dubai = get_current_weather("Dubai")
        new_york = get_current_weather("New York")
        london = get_current_weather("London")
        tokyo = get_current_weather("Tokyo")
        los_angeles = get_current_weather("Los Angeles")
        alaska = get_current_weather("Alaska")
        rio_de_janeiro = get_current_weather("Rio de Janeiro")

        context = {
            "dubai": dubai,
            "new_york": new_york,
            "london": london,
            "tokyo": tokyo,
            "los_angeles": los_angeles,
            "alaska": alaska,
            "rio_de_janeiro": rio_de_janeiro,
        }

        return render(request, "home.html", context)
