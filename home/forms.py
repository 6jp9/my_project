from django import forms
from .models import Products
class ProductForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'stock','image']
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       # Make all fields required
       for field_name, field in self.fields.items():
           field.required = True