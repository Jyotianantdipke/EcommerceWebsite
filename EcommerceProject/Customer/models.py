from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from Accounts.models import Customer, CustomUser
from Seller.models import Laptop, Grocery, Mobile


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE, null=True)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    # def __str__(self):
    #     return f'{self.customer.name}'


class Country(models.Model):
    country_name = models.CharField(max_length=32)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=32)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=32)

    def __str__(self):
        return self.city_name


class CustomerProfile(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    Full_name = models.CharField(max_length=128)
    Mobile_no = models.IntegerField(null=True, validators=[
        MinValueValidator(1000000000, "The Mobile number must contains 10 digits only."),
        MaxValueValidator(9999999999, "The Mobile number must contains 10 digits only.")])
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    pin_code = models.IntegerField(null=True,
                                   validators=[MinValueValidator(100000, 'The PIN code must contains 6 digits only. '),
                                               MaxValueValidator(999999, 'The PIN code must contains 6 digits only. ')])
    address = models.CharField(max_length=512, null=True)
