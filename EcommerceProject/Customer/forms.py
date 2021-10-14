import datetime
from django.core import validators
from django import forms
from django.db.models import fields

from .models import CustomerProfile, Country, State, City,Addresses



class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerProfile
        exclude=['customer']
        widgets = {
            'DOB': DateInput(),
            'gender':forms.RadioSelect(attrs={
            'display': 'inline-block',})
        }

    field_order=['first_name','last_name','gender','DOB']

       
    
class AddressesForm(forms.ModelForm):
    
    class Meta:
        model=Addresses
        field='__all__'
        exclude=['customer']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('state_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('country_name')

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.id:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('state_name')

    


    

    





