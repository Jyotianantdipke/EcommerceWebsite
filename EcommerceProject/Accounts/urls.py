
from django.urls import path,include
from .views import seller_loginview,customer_loginview,seller_registerview,customer_registerview,customer_logout_view,seller_logout_view



urlpatterns=[
    path('customerregister/',customer_registerview,name='customerregister'),
    path('customerlogin/',customer_loginview,name='customerlogin'),
    path('sellerregister/',seller_registerview,name='sellerregister'),
    path('sellerlogin/',seller_loginview,name='sellerlogin'),
    path('customerlogout/',customer_logout_view,name='customerlogout'),
    path('sellerlogout/',seller_logout_view,name='sellerlogout'),

    path('',include('django.contrib.auth.urls'))

]