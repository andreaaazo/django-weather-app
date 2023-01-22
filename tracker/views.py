import requests
import os

from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.views import View

from .forms import SearchCityForm

from .models import FavouriteCity


# Create your functions here
def get_3hrs_temperature_forecast(city):
    """Gets temperature of 7 days with a gap of 3 hours with OpenWeather

    RETURNS: list or None if invalid city

    INDEX: represents the gap of 3 hours

    VALUES: temperature, icon_id

    EXAMPLE: [[23, "2d"], [26, "4d"], ...]
    """

    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
    ).json()

    try:

        forecast_temperature = list()
        forecast_icons = list()

        for i in range(0, 40):
            forecast_temperature.append(round(weather_data["list"][i]["main"]["temp"]))
            forecast_icons.append(weather_data["list"][i]["weather"][0]["icon"])

        return forecast_temperature, forecast_icons

    except KeyError:
        return None


def get_current_weather(city):
    """Gets current weather based on a city with OpenWeather

    RETURNS: dict or None if invalid city

    VALUES: city, country, main, icon, description, wind, wind_deg, humidity, temp, temp_feel, temp_min, temp_max, time(UTC)

    """

    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    ).json()

    try:
        main = weather_data["weather"][0]["main"]

        match main:
            case "Rain":
                main = "rainy"
            case "Thunderstorm":
                main = "rainy"
            case "Drizzle":
                main = "rainy"
            case "Clouds":
                main = "cloudy"
            case "Snow":
                main = "snow"
            case _:
                main = "sunny"

        return dict(
            city=weather_data["name"],
            country=weather_data["sys"]["country"],
            main=main,
            icon=weather_data["weather"][0]["icon"],
            description=weather_data["weather"][0]["description"].capitalize(),
            wind=round(weather_data["wind"]["speed"]),
            wind_deg=round(weather_data["wind"]["deg"]),
            humidity=round(weather_data["main"]["humidity"]),
            temp=round(weather_data["main"]["temp"]),
            temp_feel=round(weather_data["main"]["feels_like"]),
            temp_min=round(weather_data["main"]["temp_min"]),
            temp_max=round(weather_data["main"]["temp_max"]),
            time=str(
                (datetime.now() + timedelta(seconds=weather_data["timezone"])).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            ),
            timezone=weather_data["timezone"] / 3600,
        )
    except KeyError:
        return None


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
