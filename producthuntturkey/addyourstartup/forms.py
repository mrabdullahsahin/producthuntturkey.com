from django.forms import ModelForm
from django import forms
from .models import AddYourStartupArea

class AddYourStartupForm(ModelForm):

    product_launch_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'
    }))

    class Meta:
        model = AddYourStartupArea
        fields = ['product_name', 'product_about_tr', 'product_about_en', 'product_twitter', 'product_owner_twitter', 'product_ph_link', 'product_website', 'product_team_size', 'product_picture', 'product_city', 'product_launch_date']