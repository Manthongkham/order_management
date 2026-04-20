from django import forms
from django.utils import timezone
from .models import Order, OrderNote


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


class OrderNoteForm(forms.ModelForm):
    class Meta:
        model = OrderNote
        fields = ['note_date', 'note_text']
        widgets = {
            'note_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'note_text': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['note_date'].initial = timezone.now().strftime('%Y-%m-%dT%H:%M')