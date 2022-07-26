from django.urls import path, include
from . import views

urlpatterns = [
    # In order to access this route you have to make the request to this URL: localhost:port#/item/
    path('', views.item_form, name="create_item"),  # Used to create new entries (CREATE)
    path('list/', views.item_list, name="list_items"),  # Used to display item list (READ)
    path('<int:id>/', views.item_form, name="update_item"),   # Used to update item values (UPDATE)
    path('delete/<int:id>/', views.item_delete, name="delete_item"),  # Used to delete item entries (DELETE)

    path('warehouse/', views.warehouse_form, name="create_warehouse"),  # Used to create new warehouse (CREATE)
]