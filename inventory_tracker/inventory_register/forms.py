from django import forms
from .models import InventoryItem

class ItemForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = ('itemName', 'itemCode', 'serialNum', 'quantity', 'warehouse')
        labels = {
            'itemName': 'Item Name',
            'itemCode': 'Item Code',
            'serialNum': 'Serial Number',
            'quantity': 'Quantity', 
            'warehouse': 'Warehouse'
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(ItemForm, self).__init__(*args, **kwargs)
    #     self.fields['warehouse'].empty_label = "Select"
    #     self.fields['itemCode'].required = False