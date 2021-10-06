
from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.homeview, name='home'),
    path('addproduct/', views.AddProductView, name='addproduct'),
    path('cfl/', views.createFakeLaptop, name='cfl'),
    path('addmobile',views.addmobile,name='addmobile'),
    path('cfm/', views.createFakeMobile, name='cfm'),
    path('cfg/', views.createFakeGrocery, name='cfg'),
    path('addlaptop/',views.addlaptop,name='addlaptop'),
    path('addgrocery/',views.addgrocery,name='addgrocery'),
    path('updatemobile/<int:id>/', views.update_mobile, name='updatemobile'),
    path('updatelaptop/<int:id>/', views.update_laptop, name='updatelaptop'),
    path('updategrocery/<int:id>/', views.update_grocery, name='updategrocery'),
    path('deletemobile/<int:id>/', views.delete_mobile, name='deletemobile'),
    path('deletelaptop/<int:id>/', views.delete_laptop, name='deletelaptop'),
    path('deletegrocery/<int:id>/',views.delete_grocery,name='deletegrocery'),
    path('showselleresproduct/',views.show_product_seller,name='showselleresproduct'),

]