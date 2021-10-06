import django_filters
from .models import Laptop, Mobile, Grocery


class LaptopFilter(django_filters.FilterSet):
    class Meta:
        model = Laptop
        fields = '__all__'
        exclude = ['image', 'seller', ]


class MobileFilter(django_filters.FilterSet):
    class Meta:
        model = Mobile
        fields = '__all__'
        exclude = ['image', 'seller', ]


class GroceryFilter(django_filters.FilterSet):
    class Meta:
        model = Grocery
        fields = '__all__'
        exclude = ['image', 'seller', ]
