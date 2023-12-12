# your_app/urls.py
from django.urls import path
from .views import milk_collection_graph

urlpatterns = [
    path('milk-collection-graph/', milk_collection_graph, name='milk_collection_graph'),
]
