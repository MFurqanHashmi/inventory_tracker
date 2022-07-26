from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import InventoryItem

# Create your views here.

def item_list(request):
    context = {'item_list':InventoryItem.objects.all()}

    return render(request, "inventory_register/item_list.html",context)

# GET/POST requests for inset/update operations
def item_form(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, "inventory_register/item_form.html", {'form':form})
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Form Entries were invalid")
        return redirect('/item/list')

# Delete operation
def item_delete(request):
    return