from django.core import validators
from django import forms
from .models import CustomerProfile,Country,State,City

def len_number(number):
    count=0
    while number>0:
        count+=1
        number=number//10
    return count



class CustomerProfileForm(forms.ModelForm):
    flat=forms.CharField(max_length=64,required=False)
    area=forms.CharField(max_length=64,required=False)
    landmark=forms.CharField(max_length=64,required=False)
    class Meta:
        model=CustomerProfile
        fields='__all__'
        exclude=['customer','address']
        labels={
            'flat':'Flat, House no., Building, Company, Appartment',
            'area':'Area, Colony, Street, Sector, Village',
            'landmark':'Landmark',
            'city':'Town/City',
            'Mobile_no':'Mobile Number',
            'pin_code':'PIN code',
            'state':'State/Province/Region',
            'country':'Country/Region',
            'Full_name':'Full name (First and Last name)'
        }

        # widgets={
        #     'Mobile_no':'10-digit mobile number without prefixex',
        #     'pin_code':'6 digits[0-9] PIN code',
        #     'landmark':'E.g. Near AIIMS Flyover, Behind Regal Cinema,etc'
        # }

    # def clean(self):
    #     all_data=super().clean()
    #     pin_code=all_data.get('pin_code')
    #     Mobile_no=all_data.get('Mobile_no')
    #     # if len_number(pin_code) > 6 or len_number(pin_code) < 6:
    #     #     raise forms.ValidationError("Pincode should be 6 digits only")
    #     #
    #     # if len_number(Mobile_no) > 10 or len_number(Mobile_no) < 10:
        #     raise forms.ValidationError("Mobile Number should be 10 digits only")






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
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('country_name')

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('state_name')


