from django.shortcuts import render
from django.views.generic import CreateView
from .forms import BerryUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = BerryUserCreationForm
    success_url = reverse_lazy("login")
