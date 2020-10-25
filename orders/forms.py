from django.forms import ModelForm
from django import forms
from .models import Order

class OrderForm(ModelForm):
    OPTIONS = (
        ('',''),
        ('Netbanking','Netbanking'),
        ('Wallet','Wallet'),
        ('Cash on Delivery', 'Cash on Delivery')
    )
    OPTIONS2 = (
        ('Processing', 'Processing'),
        ('Dispatched ', 'Dispatched '),
        ('Delivered', 'Delivered'),
        
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','amount','order_status']