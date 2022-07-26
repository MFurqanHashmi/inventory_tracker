from django.shortcuts import render
from .forms import ItemForm

# Create your views here.

def item_list(request):
    return render(request, "inventory_register/item_list.html")

# GET/POST requests for inset/update operations
def item_form(request):
    form = ItemForm()
    return render(request, "inventory_register/item_form.html", {'form':form})

# Delete operation
def item_delete(request):
    return