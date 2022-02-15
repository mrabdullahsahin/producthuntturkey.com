from django.forms import ModelForm
from django import forms
from .models import AddYourStartupArea
from products.models import City, TeamSize

class AddYourStartupForm(ModelForm):
    product_name = forms.CharField(max_length = 250, required=True)
    product_about_en = forms.CharField(required=True,widget=forms.widgets.Textarea())
    product_about_tr = forms.CharField(required=True,widget=forms.widgets.Textarea())
    product_twitter = forms.CharField(max_length = 250, required=False)
    product_owner_twitter = forms.CharField(max_length = 250, required=False)
    product_ph_link = forms.URLField(max_length = 250, required=True)
    product_website = forms.URLField(max_length = 250, required=True)
    product_team_size = forms.ModelChoiceField(queryset=TeamSize.objects.all(), required=True)
    product_picture = forms.ImageField(required=True, widget=forms.FileInput(attrs={'accept': '.gif, .jpg, .jpeg, .png'}))
    product_city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    product_launch_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AddYourStartupArea
        fields = ['product_name', 'product_about_tr', 'product_about_en', 'product_twitter', 'product_owner_twitter', 'product_ph_link', 'product_website', 'product_team_size', 'product_picture', 'product_city', 'product_launch_date']