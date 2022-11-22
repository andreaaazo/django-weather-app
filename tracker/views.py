from django.shortcuts import render

# Create your views here.
def response(request):
    return render(request, "tracker.html")
