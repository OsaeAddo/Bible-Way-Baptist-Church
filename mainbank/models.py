from django.db import models
from django.contrib.auth.models import User
from django.forms import UUIDField
import uuid


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True, default="images/user.svg.png")
    balance = models.FloatField(default=0, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return f"{self.user.username}"


class BankAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    account_number = models.UUIDField(primary_key=True, default=uuid.uuid4)


    def __str__(self):
        return f"{self.account_number}({self.customer.user.username})"
