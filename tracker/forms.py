from django import forms
from django.utils.translation import gettext_lazy as _


class SearchCityForm(forms.Form):
    city = forms.CharField(
        max_length=30,
        label="",
        widget=forms.TextInput(attrs={"placeholder": _("London")}),
    )
