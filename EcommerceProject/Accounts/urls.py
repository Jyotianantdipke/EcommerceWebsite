
from django.urls import path
from .views import seller_loginview,ActivateAccount, customer_loginview,seller_registerview,customer_registerview,customer_logout_view,seller_logout_view



urlpatterns=[
    path('customerregister/',customer_registerview,name='customerregister'),
    path('customerlogin/',customer_loginview,name='customerlogin'),
    path('sellerregister/',seller_registerview,name='sellerregister'),
    path('sellerlogin/',seller_loginview,name='sellerlogin'),
    path('customerlogout/',customer_logout_view,name='customerlogout'),
    path('sellerlogout/',seller_logout_view,name='sellerlogout'),
    # path('send_otp/',send_otp,name='send_otp'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]