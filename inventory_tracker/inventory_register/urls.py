from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.item_form), # In order to access this route you have to make the request to this URL: localhost:port#/item/
    path('list/', views.item_list)
]