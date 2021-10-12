
from django.urls import path
from django.contrib.auth import views as view
from . import views

urlpatterns = [
    path('sellerhome/',views.seller_home, name='sellerhome'),
    path('customer_to_seller_home/', views.customer_to_seller_home, name='customer_to_seller_home'),

    path('addproduct/', views.add_product_view, name='addproduct'),

    path('createlaptop/', views.add_laptop, name='createlaptop'),
    path('cfl/', views.createFakeLaptop, name='cfl'),
    path('updatelaptop/<int:id>', views.update_laptop, name='updatelaptop'),
    path('deletelaptop/<int:id>', views.delete_laptop, name='deletelaptop'),

    path('createmobile/', views.add_mobile, name='createmobile'),
    path('cfm/', views.createFakeMobile, name='cfm'),
    path('updatemobile/<int:id>', views.update_mobile, name='updatemobile'),
    path('deletemobile/<int:id>', views.delete_mobile, name='deletemobile'),

    path('creategrocery/', views.add_grocery, name='creategrocery'),
    path('cfg/', views.createFakeGrocery, name='cfg'),
    path('updategrocery/<int:id>', views.update_grocery, name='updategrocery'),
    path('deletegrocery/<int:id>', views.delete_grocery, name='deletegrocery'),

    path('showallproducts/', views.show_all_products, name='showallproducts'),

    path('password_reset_seller/', view.PasswordResetView.as_view(template_name='Seller/password_reset.html'),
     name='password_reset_seller'),

    path('seller/password_reset/done/', view.PasswordResetDoneView.as_view(template_name='Seller/password_reset_done.html'),
     name='password_reset_done'),

    path('seller/reset/<uidb64>/<token>/', view.PasswordResetConfirmView.as_view(template_name="Seller/password_reset_confirm.html"),
         name='password_reset_confirm'),

    path('seller/reset/done/', view.PasswordResetCompleteView.as_view(template_name='Seller/password_reset_complete.html'),
         name='password_reset_complete'),

]