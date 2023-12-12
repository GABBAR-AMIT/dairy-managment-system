# views.py
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from .models import MilkCollection
import json
from datetime import date

def milk_collection_graph(request):
    data = MilkCollection.objects.values_list('date', 'total')

    # Convert date objects to string representations
    chart_data = [{'date': entry[0].strftime('%Y-%m-%d'), 'total': entry[1]} for entry in data]

    # Convert the data to JSON
    chart_data_json = json.dumps(chart_data, cls=DjangoJSONEncoder)

    return render(request, 'milk_collection_graph.html', {'chart_data': chart_data_json})
