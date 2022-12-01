from django import forms


class SearchCityForm(forms.Form):
    city = forms.CharField(
        max_length=30,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "London"
            }
        )
    )