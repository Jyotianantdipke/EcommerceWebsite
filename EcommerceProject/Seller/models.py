from django.db import models
from Accounts.models import Seller, Customer

# Create your models here.
class Laptop(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=True)
    brand_name=models.CharField(max_length=50, null=True)
    RAM=models.IntegerField(null=True)
    ROM=models.IntegerField(null=True)
    processor=models.CharField(max_length=50, null=True)
    OS = models.CharField(max_length=64, null=True)
    warranty = models.IntegerField(null=True)
    price=models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    image = models.FileField(upload_to='images/', default='Laptop.jpg', blank=True)

class Mobile(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True )
    brand_name=models.CharField(max_length=50, null=True)
    RAM = models.IntegerField(null=True)
    ROM = models.IntegerField(null=True)
    processor = models.CharField(max_length=50, null=True)
    warranty=models.IntegerField(null=True)
    price=models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    image = models.FileField(upload_to='Mobile/images/', default='Mobile.jpg', blank=True)

class Grocery(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.FloatField()
    warranty = models.IntegerField()
    image = models.FileField(upload_to='Grocery/images/', default='Grocery.jpg',  blank=True)

    def __str__(self):
        return self.product_name

class Cosmetics(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    Price = models.FloatField(max_length=64)
    stock = models.IntegerField(null=True)
    image = models.FileField(upload_to='Cosmetics/images/', default='Grocery.jpg', blank=True)

class Clothing(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    Size = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    Price = models.FloatField(max_length=64)
    stock = models.IntegerField(null=True)
    image = models.FileField(upload_to='Clothing/images/', default='Grocery.jpg', blank=True)


class Footwear(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    Size = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    Price = models.FloatField(max_length=64)
    stock = models.IntegerField(null=True)
    image = models.FileField(upload_to='Footwear/images/', default='Grocery.jpg', blank=True)

