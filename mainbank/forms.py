from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]


# Add CustomerForms

class CustomerForm(forms.ModelForm):
    class Meta: 
        model = models.Customer
        fields = [
            'mobile'
        ]


class TransferForm(forms.ModelForm):
    class Meta: 
        model = models.Transfer
        fields = [
            'amount',
            'to_account',
            'routing_number'
        ]
        widgets = {
            'amount': forms.TextInput(attrs={
                'placeholder': 'amount',
            }),
            'to_account': forms.TextInput(attrs={
                'placeholder': 'enter recipient account'
            }),
            'routing_number': forms.TextInput(attrs={
                'placeholder': 'enter routing number'
            }),
        }