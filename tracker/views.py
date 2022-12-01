from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import SearchCityForm

from .models import FavouriteCity

from api.get_current_weather import get_current_weather
from api.get_3hrs_forecast import get_3hrs_temperature_forecast

# Create your views here.
class TrackerPageView(View):
    def get(self, request, *args, **kwargs):
        default_city_current_weather = get_current_weather("Zurich")
        default_city_forecast_weather = get_3hrs_temperature_forecast("Zurich")

        context = {
            "current_weather": default_city_current_weather,
            "search_city_form": SearchCityForm,
            "city_forecast": default_city_forecast_weather,
        }

        if request.user.is_authenticated:
            favourites = dict()

            for i in FavouriteCity.objects.filter(favourite=request.user).all():
                favourites[i] = get_current_weather(i)

            context["favourites"] = favourites

        return render(request, "tracker.html", context)

    def post(self, request, *args, **kwargs):
        form = SearchCityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]

            city_current_weather = get_current_weather(city)
            city_forecast = get_3hrs_temperature_forecast(city)

            context = {
                "city_forecast": city_forecast,
                "current_weather": city_current_weather,
                "search_city_form": SearchCityForm,
            }

            return render(request, "tracker.html", context)


class TrackerAddFavourite(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        city = kwargs["city"]
        if not FavouriteCity.objects.filter(city=city).exists():
            FavouriteCity(city=city).save()
            FavouriteCity.objects.get(city=city).favourite.add(request.user)

        return redirect("tracker")


@login_required
class TrackerRemoveFavourite(View):
    def get(self, request, *args, **kwargs):
        city = kwargs["city"]
        FavouriteCity.objects.get(city=city).favourite.remove(request.user)

        return redirect("tracker")
