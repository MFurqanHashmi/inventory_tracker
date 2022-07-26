from django import forms
from .models import InventoryItem

class ItemForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = ('itemName', 'itemCode', 'serialNum', 'warehouse')