from django.contrib.gis.geoip2 import GeoIP2


def geolocate_city(request):
    g = GeoIP2()
    ip = request.META.get("REMOTE_ADDR")
    if not ip == "127.0.0.1" and ip:
        return g.city(ip)["city"]
    else:
        return "Zürich"  # default city
