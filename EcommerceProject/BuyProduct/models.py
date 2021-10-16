from django.db import models
from Accounts.models import Customer
from Seller.models import Laptop,Mobile,Grocery
from Customer.models import Addresses
# Create your models here.

payment_mode=(
    ('Online',"Online"),
    ('Cash on Delivery','Cash on Delivery')
)


class OrderedProduct(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    laptop=models.ForeignKey(Laptop,on_delete=models.CASCADE,null=True)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,null=True)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, null=True)
    price=models.IntegerField()
    quantity=models.IntegerField()
    delivery_address=models.OneToOneField(Addresses,on_delete=models.CASCADE)
    payment_mode=models.CharField(max_length=16,choices=payment_mode)
    order_date=models.DateField()

    # def __str__(self):
    #     return f'{self.customer},{self.delivery_address},{self.payment_mode} {self.mobile.name}'