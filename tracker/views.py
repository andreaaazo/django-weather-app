from django.shortcuts import render
from .geolocation import geolocate_city
from .api import current_weather, forecast_4_hour_weather
from .forms import CityForm
from .models import FavoriteCity

# Create your views here.
def tracker_view(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]

    elif request.method == "GET":
        form = CityForm()
        city = geolocate_city(request)

    current = current_weather(city)
    hourly_forecast = forecast_4_hour_weather(city)

    context = {
        "current_weather": current,
        "hourly_forecast": hourly_forecast,
        "form": form,
    }

    for i in FavoriteCity.objects.filter(user=request.user):
        print(i)



    return render(request, "tracker.html", context)