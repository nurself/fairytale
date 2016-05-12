from django import forms
from .models import *

class SuitForm(forms.ModelForm):
    class Meta:
        model = Suit
        fields = ('name', 'picture','vendor_code','year_issue','details','colour','rent_price','item_price','note','branch',)


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ('protocol_num', 'start_date','end_date','people','reserve_sum','total_price','user','published_date','is_returned',)