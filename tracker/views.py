from django.shortcuts import render, redirect
from django.views import View

from .forms import SearchCityForm

from .models import FavouriteCity

from api.weather_prevision import get_3hrs_temperature_forecast, get_current_weather


# Create your views here.
class TrackerPageView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            favourites = dict()

            for i in FavouriteCity.objects.filter(favourite=request.user).all():
                favourites[i] = get_current_weather(i)

            if favourites:
                kwargs["favourites"] = favourites
            else:
                kwargs["favourites"] = None
        else:
            kwargs["favourites"] = None

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        default_city_current_weather = get_current_weather("Zurich")
        (
            default_city_forecast_temperature,
            default_city_forecast_icons,
        ) = get_3hrs_temperature_forecast("Zurich")

        context = {
            "current_weather": default_city_current_weather,
            "search_city_form": SearchCityForm,
            "city_forecast": default_city_forecast_temperature,
            "city_forecast_icons": default_city_forecast_icons,
            "favourites": kwargs["favourites"],
        }

        return render(request, "tracker.html", context)

    def post(self, request, *args, **kwargs):
        form = SearchCityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]

            city_current_weather = get_current_weather(city)

            (
                default_city_forecast_temperature,
                default_city_forecast_icons,
            ) = get_3hrs_temperature_forecast(city)

            context = {
                "city_forecast": default_city_forecast_temperature,
                "city_forecast_icons": default_city_forecast_icons,
                "current_weather": city_current_weather,
                "search_city_form": SearchCityForm,
                "favourites": kwargs["favourites"],
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


class TrackerRemoveFavourite(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        city = kwargs["city"]
        FavouriteCity.objects.get(city=city).favourite.remove(request.user)

        return redirect("tracker")
