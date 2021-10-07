
from django.urls import path,include
from .views import seller_loginview,customer_loginview,change_pass_view,seller_registerview,customer_registerview,customer_logout_view,seller_logout_view
from django.contrib.auth import views


urlpatterns=[
    path('customerregister/',customer_registerview,name='customerregister'),
    path('customerlogin/',customer_loginview,name='customerlogin'),
    path('sellerregister/',seller_registerview,name='sellerregister'),
    path('sellerlogin/',seller_loginview,name='sellerlogin'),
    path('customerlogout/',customer_logout_view,name='customerlogout'),
    path('sellerlogout/',seller_logout_view,name='sellerlogout'),
    path('changepassword/',change_pass_view,name='changepassword'),

    path('reset_password/', views.PasswordResetView.as_view(template_name='Account/password_reset_form.html'),
         name='reset_password'),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name='Account/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='Account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         views.PasswordResetCompleteView.as_view(template_name='Account/password_reset_complete.html'),
         name='password_reset_complete')

]