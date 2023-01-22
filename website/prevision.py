import requests
import os
from datetime import datetime, timedelta

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")


def get_3hrs_temperature_forecast(city: str):
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


def get_current_weather(city: str):
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
