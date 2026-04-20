from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'sales_order_number',
            'sold_to_name',
            'ship_to_name',
            'production_block',
            'block_type',
            'document_cutoff_date',
        ]