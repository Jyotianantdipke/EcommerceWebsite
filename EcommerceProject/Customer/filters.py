import django_filters
from Seller.models import Laptop, Mobile, Grocery
from django import forms

class LaptopFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Laptop
        fields = '__all__'
        exclude = ['image', 'seller', 'stock','warranty','price']


class MobileFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='gte')
    class Meta:
        model = Mobile
        fields = '__all__'
        exclude = ['image', 'seller', 'stock','warranty','price']

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


class GroceryFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Grocery
        fields = '__all__'
        exclude = ['image', 'seller', 'stock','warranty','price']