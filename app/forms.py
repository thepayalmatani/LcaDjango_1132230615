from django import forms
from .models import product  # Import the correct model class

class productForm(forms.ModelForm):
    class Meta:
        model = product  # Correctly reference the model
        fields = ['name', 'category', 'price', 'sales']  # List of fields you want to include in the form
