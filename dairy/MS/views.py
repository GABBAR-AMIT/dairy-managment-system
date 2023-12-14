# views.py
from django.shortcuts import render,redirect
from django.core.serializers.json import DjangoJSONEncoder
from .models import MilkCollection
import json
from datetime import date
from .forms import MilkCollectionForm

def milk_collection_graph(request):
    data = MilkCollection.objects.values_list('date', 'total')

    # Convert date objects to string representations
    chart_data = [{'date': entry[0].strftime('%Y-%m-%d'), 'total': entry[1]} for entry in data]

    # Convert the data to JSON
    chart_data_json = json.dumps(chart_data, cls=DjangoJSONEncoder)

    return render(request, 'milk_collection_graph.html', {'chart_data': chart_data_json})

def add_milk_collection(request):
    if request.method == 'POST':
        form = MilkCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('milk_collection_graph')  # Redirect to the graph page after successful submission
    else:
        form = MilkCollectionForm()

    return render(request, 'add_milk_collection.html', {'form': form})

def delete_milk_collection(request, collection_id):
    milk_collection = MilkCollection.objects.get(collection_id=collection_id)
    milk_collection.delete()
    return redirect('milk_collection_graph')  # Redirect to the graph page after successful deletion