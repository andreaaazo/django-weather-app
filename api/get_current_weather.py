import requests


def get_current_weather(city: str):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c40b441495d816083e64697672168f11&units=metric"
    ).json()

    try:
        return dict(
            city=weather_data["name"],
            country=weather_data["sys"]["country"],
            temp=round(weather_data["main"]["temp"]),
            temp_min=round(weather_data["main"]["temp_min"]),
            temp_max=round(weather_data["main"]["temp_max"]),
        )
    except KeyError:
        return None
