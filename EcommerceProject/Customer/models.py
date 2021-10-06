
from django.db import models
from Accounts.models import Customer,CustomUser
from Seller.models import Laptop,Grocery,Mobile

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    laptop=models.ForeignKey(Laptop,on_delete=models.CASCADE,null=True)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,null=True)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, null=True)
    price=models.IntegerField()
    quantity=models.IntegerField()

    # def __str__(self):
    #     return f'{self.customer.name}'

class Country(models.Model):
    country_name=models.CharField(max_length=32)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name=models.CharField(max_length=32)

    def __str__(self):
        return self.state_name

class City(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=32)


    def __str__(self):
        return self.city_name


class CustomerProfile(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=124)


class CustomerAddress(models.Model):
    customer_profile=models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,blank=True, null=True)
