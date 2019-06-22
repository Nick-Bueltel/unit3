from django.forms import ModelForm, Form, CharField, PasswordInput
from .models import Item

class ItemForm(ModelForm):
    class Meta: 
        model = Item
        fields = ['description']