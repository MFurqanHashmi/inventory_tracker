from django.shortcuts import render, redirect
from .forms import ItemForm

# Create your views here.

def item_list(request):
    return render(request, "inventory_register/item_list.html")

# GET/POST requests for inset/update operations
def item_form(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, "inventory_register/item_form.html", {'form':form})
    else:
        print("****************////////////// POST REQUEST //////////////****************")
        form = ItemForm(request.POST)
        if form.is_valid():
            print("////////////// FORM IS VALID //////////////")
            form.save()
        return redirect('/item/list')

# Delete operation
def item_delete(request):
    return