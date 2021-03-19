from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        #model to user
        model = Order
        # all the fields(can specify particular field in list)
        fields = '__all__'
        
        