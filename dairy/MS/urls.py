# your_app/urls.py
from django.urls import path
from .views import milk_collection_graph
from .views import add_milk_collection, delete_milk_collection

urlpatterns = [
    path('milk-collection-graph/', milk_collection_graph, name='milk_collection_graph'),
    path('add/', add_milk_collection, name='add_milk_collection'),
    path('delete/<str:collection_id>/', delete_milk_collection, name='delete_milk_collection'),
]