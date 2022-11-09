from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DataberryUserCreationForm
from django.urls import reverse_lazy


# Create your views here.
class SignUpView(CreateView):
    form_class = DataberryUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
