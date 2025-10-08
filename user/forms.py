from django import forms
from django.contrib.auth.models import User
from .models import Customers,Merchants

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter password'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['first_name','last_name','phone','address']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'type': 'tel','class': 'form-control', 'placeholder': 'Phone'},),
            'address': forms.Textarea(attrs={'rows': 3,'class': 'form-control', 'placeholder': 'Address'}),
        }


class MerchantDetailsForm(forms.ModelForm):
    class Meta:
        model = Merchants
        fields = ['business_name','phone','address']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business Name'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'rows': 3,'class': 'form-control', 'placeholder': 'Address'}),
           }