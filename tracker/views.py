from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TrackerPageView(TemplateView):
    template_name = "tracker.html"
