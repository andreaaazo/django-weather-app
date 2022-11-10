import requests
from datetime import datetime, timedelta


def current_weather(city):
    current_city_weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c40b441495d816083e64697672168f11"
    ).json()

    current_weather = {
        "city": current_city_weather["name"],
        "country": current_city_weather["sys"]["country"],
        "description": current_city_weather["weather"][0]["description"],
        "icon": current_city_weather["weather"][0]["icon"],
        "temp": int(current_city_weather["main"]["temp"] - 273.15),
        "temp_min": int(current_city_weather["main"]["temp_min"] - 273.15),
        "temp_max": int(current_city_weather["main"]["temp_max"] - 273.15),
        "wind_speed": round(current_city_weather["wind"]["speed"], 1),
        "wind_direction": round(current_city_weather["wind"]["deg"], 1),
        "humidity": current_city_weather["main"]["humidity"],
        "time": str(
            (
                datetime.now() + timedelta(seconds=current_city_weather["timezone"])
            ).strftime("%Y-%m-%d %H:%M:%S")
        ),
        "timezone": current_city_weather["timezone"] / 3600,
        "hour": (
            datetime.fromtimestamp(current_city_weather["dt"])
            + timedelta(hours=current_city_weather["timezone"] / 3600)
        ).hour,
    }

    return current_weather


def forecast_4_hour_weather(city):
    forecast_city_weather = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=c40b441495d816083e64697672168f11"
    ).json()

    timezone = forecast_city_weather["city"]["timezone"] / 3600

    forecast_weather = {
        "1": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][0]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][0]["main"]["temp"] - 273.15),
        },
        "2": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][1]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][1]["main"]["temp"] - 273.15),
        },
        "3": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][2]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][2]["main"]["temp"] - 273.15),
        },
        "4": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][3]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][3]["main"]["temp"] - 273.15),
        },
        "5": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][4]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][4]["main"]["temp"] - 273.15),
        },
        "6": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][5]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][5]["main"]["temp"] - 273.15),
        },
        "7": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][6]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][6]["main"]["temp"] - 273.15),
        },
        "8": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][7]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][7]["main"]["temp"] - 273.15),
        },
        "9": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][8]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][8]["main"]["temp"] - 273.15),
        },
        "10": {
            "hour": (
                datetime.strptime(
                    forecast_city_weather["list"][9]["dt_txt"], "%Y-%m-%d %H:%M:%S"
                )
                + timedelta(hours=timezone)
            ).hour,
            "temp": int(forecast_city_weather["list"][9]["main"]["temp"] - 273.15),
        },
    }

    return forecast_weather
