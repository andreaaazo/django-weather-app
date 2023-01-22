import requests
import os

from datetime import datetime, timedelta

from django.shortcuts import render
from django.views import View


# Create your functions here.
def get_3hrs_temperature_forecast(city) -> list:
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


def get_current_weather(city) -> dict:
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
