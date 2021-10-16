from django.urls import __path__
from django.urls import path
from .views import buynow_mobile,my_order,create_Invoice


urlpatterns=[
    path('buymobile/<int:id>',buynow_mobile,name='buymobile'),
    path('myorder/',my_order,name='myorder'),
    path('createinvoice/<int:id>',create_Invoice,name='createinvoice')
]