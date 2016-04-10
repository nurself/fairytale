from django import forms
from .models import Suit

class SuitForm(forms.ModelForm):
    class Meta:
        model = Suit
        fields = ('name', 'picture','vendor_code','year_issue','details','colour','rent_price','item_price','note','branch',)
