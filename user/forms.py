from django import forms
from django.contrib.auth.models import User
from .models import Customers,Merchants

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name','last_name','phone','address']

class MerchantDetailsForm(forms.ModelForm):
    class Meta:
        model = Merchants
        fields = ['business_name','phone','address']
