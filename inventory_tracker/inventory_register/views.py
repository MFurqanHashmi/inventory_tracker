from django.shortcuts import render

# Create your views here.

def item_list(request):
    return render(request, "inventory_register/item_list.html")

# GET/POST requests for inset/update operations
def item_form(request):
    return render(request, "inventory_register/item_form.html")

# Delete operation
def item_delete(request):
    return