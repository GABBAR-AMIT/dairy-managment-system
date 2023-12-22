from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MilkSale, MilkCollection

class MilkSaleForm(forms.ModelForm):
    class Meta:
        model = MilkSale
        fields = ['collection_number', 'customer_name', 'liter', 'price_per_liter', 'total', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional customization for the form fields if needed
        # For example, you can add placeholders or set the input types
        self.fields['date'].widget.attrs.update({'type': 'date'})

class MilkCollectionForm(forms.ModelForm):
    class Meta:
        model = MilkCollection
        fields = ['cow_number', 'collection_id', 'date', 'liter', 'price_per_liter']

class LoginForm(AuthenticationForm):
    # You can add customizations to the login form if needed
    pass
