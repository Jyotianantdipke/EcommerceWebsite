import django_filters
from .models import Laptop, Mobile, Grocery


class LaptopFilter(django_filters.FilterSet):
    min_price=django_filters.NumberFilter(name='price',lookup_expr='gte')
    max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Laptop
        fields = '__all__'
        exclude = ['image', 'seller', 'stock','warranty']


class MobileFilter(django_filters.FilterSet):
    min_price=django_filters.NumberFilter(name='price',lookup_expr='gte')
    max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Mobile
        fields = '__all__'
        exclude = ['image', 'seller', 'stock','warranty']


class GroceryFilter(django_filters.FilterSet):
    min_price=django_filters.NumberFilter(name='price',lookup_expr='gte')
    max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Grocery
        fields = '__all__'
        exclude = ['image', 'seller', 'stock','warranty']
