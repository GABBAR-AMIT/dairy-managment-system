from django.contrib import admin
from django.urls import path, include
from .views import home, login_view, logout_view, milk_collection_graph, add_milk_collection, delete_milk_collection, milk_sale_graph, create_milk_sale

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Set the login view as the default landing page
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('milk_collection_graph/', milk_collection_graph, name='milk_collection_graph'),
    path('add_milk_collection/', add_milk_collection, name='add_milk_collection'),
    path('delete_milk_collection/<int:collection_id>/', delete_milk_collection, name='delete_milk_collection'),
    path('milk_sale_graph/', milk_sale_graph, name='milk_sale_graph'),
    path('create_milk_sale/', create_milk_sale, name='create_milk_sale'),
]
