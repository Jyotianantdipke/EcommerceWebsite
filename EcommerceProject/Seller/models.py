from django.db import models
from Accounts.models import Seller, Customer
from django.core import validators

# Create your models here.
class Laptop(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    brand_name=models.CharField(max_length=50)
    RAM=models.IntegerField()
    ROM=models.IntegerField()
    processor=models.CharField(max_length=50)
    OS = models.CharField(max_length=64)
    warranty = models.IntegerField(blank=True)
    price=models.FloatField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='images/', default='Laptop.jpg', blank=True)


    def __str__(self):
        return self.name

class Mobile(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    brand_name=models.CharField(max_length=50)
    RAM = models.IntegerField(validators=[validators.MinValueValidator(1, "The RAM should be within bellow Example")])
    ROM = models.IntegerField(validators=[validators.MinValueValidator(1, "The ROM should be within bellow Example")])
    # OR
    # internal_storage=models.IntegerField()
    processor = models.CharField(max_length=50)
    warranty=models.IntegerField(blank=True, validators=[validators.MinValueValidator(1, "Warranty should be Greater than Zero")])
    price=models.FloatField(validators=[validators.MinValueValidator(1, "The Prize should be Greater than Zero")])
    stock = models.IntegerField(validators=[validators.MinValueValidator(1, "Stock should be Greater than Zero")])
    image = models.FileField(upload_to='Mobile/images/', default='Mobile.jpg', blank=True)

    def __str__(self):
        return self.name

class Grocery(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    quantity=models.FloatField(validators=[validators.MinValueValidator(1, "The Quantity should be Greater than Zero")])
    price=models.FloatField(validators=[validators.MinValueValidator(1, "The Prize should be Greater than Zero")])
    warranty = models.IntegerField(validators=[validators.MinValueValidator(1, "Warranty should be Greater than Zero")])
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

