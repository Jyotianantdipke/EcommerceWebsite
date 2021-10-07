import django_filters
from .models import Laptop, Mobile, Grocery


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
