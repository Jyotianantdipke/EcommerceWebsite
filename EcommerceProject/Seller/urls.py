
from django.urls import path

from . import views

urlpatterns = [
    path('sellerhome/',views.seller_home, name='sellerhome'),
    path('customer_to_seller_home/', views.customer_to_seller_home, name='customer_to_seller_home'),

    path('addproduct/', views.add_product_view, name='addproduct'),

    path('createlaptop/', views.add_laptop, name='createlaptop'),
    path('cfl/', views.create_fake_laptop, name='cfl'),
    path('updatelaptop/<int:id>', views.update_laptop, name='updatelaptop'),
    path('deletelaptop/<int:id>', views.delete_laptop, name='deletelaptop'),

    path('createmobile/', views.add_mobile, name='createmobile'),
    path('cfm/', views.create_fake_mobile, name='cfm'),
    path('updatemobile/<int:id>', views.update_mobile, name='updatemobile'),
    path('deletemobile/<int:id>', views.delete_mobile, name='deletemobile'),

    path('creategrocery/', views.add_grocery, name='creategrocery'),
    path('cfg/', views.create_fake_grocery, name='cfg'),
    path('updategrocery/<int:id>', views.update_grocery, name='updategrocery'),
    path('deletegrocery/<int:id>', views.delete_grocery, name='deletegrocery'),

    path('showallproducts/', views.show_all_products, name='showallproducts'),

]