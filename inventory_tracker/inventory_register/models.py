from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

# Create your models here.
class Warehouse(models.Model):
    warehouseName = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default="UNKNOWN")
    warehouseLocation = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default="UNKNOWN")
    warehouseManager = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default="UNKNOWN")

    def __str__(self):
        return self.warehouseName

class InventoryItem(models.Model):
    itemName = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default="UNKNOWN")
    itemCode = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default="UNKNOWN")
    serialNum  = models.CharField(max_length=100, validators=[MinLengthValidator(1)], default="UNKNOWN")
    quantity = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(0)
        ])
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)      #! Note: If you delete a particular warehouseName, all items under it will also be deleted in the InventoryItem table