from django import forms
from .models import Laptop, Mobile, Grocery
import math

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        exclude = ['seller']

        labels = {'name': 'Model Name',
                  'RAM': 'RAM in GB',
                  'ROM': 'RAM in GB',
                  'warranty': 'Warranty in months',
                  'price': 'Price in Rs.',
                  }
        widgets = {'RAM': forms.TextInput(attrs={'placeholder': 'Ex. 2, 4, 8, 16, 32, 64....', }),
                   'ROM': forms.TextInput(attrs={'placeholder': 'Ex. 16, 32, 64, 128, 256, 512, 1025... '}),
                   'processor': forms.TextInput(attrs={'placeholder': 'Ex. Octacore, DualCore '}),
                   'OS': forms.TextInput(attrs={'placeholder': 'Ex. Windows, Linux, MackOS '})}

    def clean_RAM(self):    # name in def should be same as per model field (Ex. RAM)
        ram=self.cleaned_data['RAM']
        print(ram)
        if ram<2:
            raise forms.ValidationError('RAM must be greater than 2. Ex 2, 4, 8, 12, 24....')
        return ram

    def clean(self):
        all_data=super().clean()
        rom=all_data['ROM']
        warranty=all_data['warranty']
        price=all_data['price']
        stock=all_data['stock']
        if rom!=16:
            raise forms.ValidationError('ROM should be positive. As per Example')
        if warranty<=0:
            raise forms.ValidationError('Warranty cant be zero as well as negative ')
        if price<=0:
            raise forms.ValidationError('Price cant be zero as well as negative ')
        if stock<=0:
            raise forms.ValidationError('Stock cant be zero as well as negative ')




class MobileModelForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
        exclude = ['seller']

        labels={'name':'Model Name',
                'RAM':'RAM in GB',
                'ROM':'RAM in GB',
                'warranty': 'Warranty in months',
                'price': 'Price in Rs.',
                }
        widgets={'RAM':forms.TextInput(attrs={'placeholder':'Ex. 2, 4, 8, 16, 32, 64....',}),
                 'ROM':forms.TextInput(attrs={'placeholder':'Ex. 16, 32, 64, 128, 256, 512, 1025... '}),
                 'processor':forms.TextInput(attrs={'placeholder':'Ex. Octacore, DualCore '})}

class GroceryModelForm(forms.ModelForm):
    class Meta:
        model=Grocery
        fields='__all__'
        exclude = ['seller']

        labels={'warranty':'Validity in months',
                'quantity':'Quantity in Kg',
                'price':'Price in Rs.'}

        widgets={'product_name':forms.TextInput(attrs={'placeholder': 'Ex. Wheat Floar'}),
                 'quantity':forms.TextInput(attrs={'placeholder': 'Ex. 0.5, 1'})}

    # def clean_quantity(self):
    #     qty=self.cleaned_data['quantity']
    #     if qty<=0:
    #         raise forms.ValidationError('Quantity should be greater than Zero')
    #     return qty
