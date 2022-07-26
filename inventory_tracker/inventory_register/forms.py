from django import forms
from .models import InventoryItem, Warehouse

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
    
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['itemName'].initial = ""
        self.fields['itemCode'].initial = ""
        self.fields['serialNum'].initial = ""
        self.fields['warehouse'].initial = ""
        # self.fields['warehouse'].empty_label = "Select Warehouse"
        self.fields['itemCode'].required = False

class WarehouseForm(forms.ModelForm):

    class Meta:
        model = Warehouse
        fields = ('warehouseName', 'warehouseLocation', 'warehouseManager')
        labels = {
            'warehouseName': 'Warehouse Name',
            'warehouseLocation': 'Location',
            'warehouseManager': 'Manager',
        }
    
    def __init__(self, *args, **kwargs):
        super(WarehouseForm, self).__init__(*args, **kwargs)
        self.fields['warehouseName'].initial = ""
        self.fields['warehouseLocation'].initial = ""
        self.fields['warehouseManager'].initial = ""