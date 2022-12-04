import requests


def get_3hrs_temperature_forecast(city: str):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=c40b441495d816083e64697672168f11&units=metric"
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
