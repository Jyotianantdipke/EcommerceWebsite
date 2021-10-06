from django.contrib import admin
from .models import CustomUser,Customer,Seller


class CustomUseradmin(admin.ModelAdmin):
    list_display=['id','mobile_no','email','password','is_customer','is_seller']
admin.site.register(CustomUser,CustomUseradmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','name']
admin.site.register(Customer,CustomerAdmin)

class SellerAdmin(admin.ModelAdmin):
    list_display=['user','company_name','gst_no','address','bank_account']
admin.site.register(Seller,SellerAdmin)
