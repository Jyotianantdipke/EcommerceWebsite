from django import forms
from .models import Laptop, Mobile, Grocery

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        exclude = ['seller']



class MobileModelForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
        exclude = ['seller']

class GroceryModelForm(forms.ModelForm):
    class Meta:
        model=Grocery
        fields='__all__'
        exclude=['seller']
