from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    # email = models.EmailField(_('email address'), unique=True)
    email = models.EmailField(unique=True)
    mobile_no=models.IntegerField(unique=True,validators=[MinValueValidator(1000000000, "The Mobile number must contains 10 digits only."),MaxValueValidator(9999999999,"The Mobile number must contains 10 digits only.")])
    is_customer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.self


class Customer(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    company_name=models.CharField(max_length=50)
    gst_no=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    bank_account=models.BigIntegerField()

    def __str__(self):
        return self.company_name


    
    


