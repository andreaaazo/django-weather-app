from django.shortcuts import render
from django.views import View

from _api import prevision

# Create your views here.
class HomePageView(View):
    def get(self, request, *args, **kwargs):

        dubai = prevision.get_current_weather("Dubai")
        new_york = prevision.get_current_weather("New York")
        london = prevision.get_current_weather("London")
        tokyo = prevision.get_current_weather("Tokyo")
        los_angeles = prevision.get_current_weather("Los Angeles")
        alaska = prevision.get_current_weather("Alaska")
        rio_de_janeiro = prevision.get_current_weather("Rio de Janeiro")

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
