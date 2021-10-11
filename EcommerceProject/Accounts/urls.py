
from django.urls import path
from .views import change_pass_view_customer,customuser_activation, change_pass_view_seller, seller_loginview,send_otp,email_verification, customer_loginview,seller_registerview,customer_registerview,customer_logout_view,seller_logout_view
from django.contrib.auth import views


urlpatterns=[
    path('customerregister/',customer_registerview,name='customerregister'),
    path('customerlogin/',customer_loginview,name='customerlogin'),
    path('sellerregister/',seller_registerview,name='sellerregister'),
    path('sellerlogin/',seller_loginview,name='sellerlogin'),
    path('customerlogout/',customer_logout_view,name='customerlogout'),
    path('sellerlogout/',seller_logout_view,name='sellerlogout'),
    path('send_otp/',send_otp,name='send_otp'),
    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('emailverify/',email_verification,name='emailverify'),

    path('changepasswordcustomer/',change_pass_view_customer,name='changepasswordcustomer'),
    path('changepasswordseller/',change_pass_view_seller,name='changepasswordseller'),
    path('useractivation',customuser_activation,name='useractivation'),
    # path('reset_password/', views.PasswordResetView.as_view(template_name='Customer/password_reset_form.html'),
    #      name='reset_password'),
    # path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name='Customer/password_reset_done.html'),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      views.PasswordResetConfirmView.as_view(template_name='Customer/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('password_reset_complete/',
    #      views.PasswordResetCompleteView.as_view(template_name='Customer/password_reset_complete.html'),
    #      name='password_reset_complete'),
    
    
]