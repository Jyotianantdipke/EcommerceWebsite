from django.urls import path
from . import views


urlpatterns=[
    path('showlaptop/',views.showlaptop, name='showlaptop'),
    path('showmobile/', views.showMobile, name='showmobile'),
    path('showgrocery/', views.showGrocery, name='showgrocery'),
    path('customerlaptopitem/<int:pk>', views.Laptopview, name='customerlaptopitem'),
    path('customermobileitem/<int:pk>', views.Mobileview, name='customermobileitem'),
    path('customergroceryitem/<int:pk>', views.Groceryview, name='customergroceryitem'),
    path('showcart/', views.show_cart, name='showcart'),
    path('shopnow/', views.shop_now, name='shopnow'),
    path('cartview/', views.Cartview, name='cartview'),
    path('deleteitem/<int:pk>', views.Deleteitemview, name='deleteitem'),
    path('customerupdateitem/<int:pk>', views.Updateallitemview, name='customerupdateitem'),
    path('customerprofile/',views.create_profile_view,name='customerprofile'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]
