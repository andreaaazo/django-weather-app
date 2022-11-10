from django.shortcuts import render, redirect
from .geolocation import geolocate_city
from .api import current_weather, forecast_4_hour_weather
from .forms import CityForm
from .models import City
from django.contrib.auth.decorators import login_required

# Create your views here.
def tracker_view(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]

    else:
        form = CityForm()
        city = geolocate_city(request)

    current = current_weather(city)
    hourly_forecast = forecast_4_hour_weather(city)

    context = {
        "current_weather": current,
        "hourly_forecast": hourly_forecast,
        "form": form,
    }

    if request.user.is_authenticated:
        favourites = City.objects.filter(favourites=request.user).all()
        favourites_list = dict()
        for i in favourites:
            favourites_list[i] = current_weather(i)

        context["favourites"] = favourites_list

    return render(request, "tracker.html", context)


@login_required
def add_to_favorites(request, city):
    if City.objects.filter(city=city).exists():
        pass
    else:
        add_city = City(city=city)
        add_city.save()

    id = City.objects.get(city=city).id
    city = City.objects.get(id=id)
    city.favourites.add(request.user)

    return redirect("tracker")


@login_required
def remove_to_favorites(request, city):
    id = City.objects.get(city=city).id
    city = City.objects.get(id=id)
    city.favourites.remove(request.user)

    return redirect("tracker")
