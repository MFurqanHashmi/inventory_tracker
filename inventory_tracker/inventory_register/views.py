from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import InventoryItem

# Create your views here.

def item_list(request):
    context = {'item_list':InventoryItem.objects.all()}

    return render(request, "inventory_register/item_list.html",context)

# GET/POST requests for create/update operations
def item_form(request,id=0):
    if request.method == "GET":
        # If the id is default value of 0 we assume it's the create operation
        if id==0:
            form = ItemForm()
        # This will pre-populate values into the fields since we'll be editing them       
        else:
            item = InventoryItem.objects.get(pk=id)
            form = ItemForm(instance=item)
        return render(request, "inventory_register/item_form.html", {'form':form})
    else:
        if id==0:
            form = ItemForm(request.POST)
        else:
            item = InventoryItem.objects.get(pk=id)
            form = ItemForm(request.POST, instance=item)
        
        if form.is_valid():
            form.save()
        else:
            print("Form Entries were invalid")
        return redirect('/item/list')

# Delete operation
def item_delete(request):
    return