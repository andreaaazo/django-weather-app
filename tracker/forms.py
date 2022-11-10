from django import forms


class CityForm(forms.Form):
    city = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "placeholder": "ex. London",
                "class": "form-control bg-surface-variant",
                "id": "InputCity",
            }
        ),
        label="",
    )
