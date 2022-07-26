from django.db import models

# Create your models here.
class Warehouse(models.Model):
    warehouseName = models.CharField(max_length=100)

class InventoryItem(models.Model):
    itemName = models.CharField(max_length=100)
    itemCode = models.CharField(max_length=100)
    serialNum  = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)      #! Note: If you delete a particular warehouseName, all items under it will also be deleted in the InventoryItem table