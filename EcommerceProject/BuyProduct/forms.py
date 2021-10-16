from django import forms
from .models import OrderedProduct


class OrderedProductForm(forms.ModelForm):
    class Meta:
        model=OrderedProduct
        field='__all__'
        exclude=['customer','laptop','mobile','grocery','price','quantity','order_date']

