from django.urls import __path__
from django.urls import path
from .views import buynow_mobile,my_order,generate_pdf,buy_cart_product


urlpatterns=[
    path('buymobile/<int:id>',buynow_mobile,name='buymobile'),
    path('myorder/',my_order,name='myorder'),
    path('generatepdf/<int:id>',generate_pdf,name='generatepdf'),
    path('buycartproduct/',buy_cart_product,name='buycartproduct'),

]