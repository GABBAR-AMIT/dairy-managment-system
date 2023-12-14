# forms.py
from django import forms
from .models import MilkCollection

class MilkCollectionForm(forms.ModelForm):
    class Meta:
        model = MilkCollection
        fields = ['cow_number', 'collection_id', 'date', 'liter', 'price_per_liter']
