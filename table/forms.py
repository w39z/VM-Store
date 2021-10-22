from django.forms import ModelForm
from .models import Item


class OrderForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
