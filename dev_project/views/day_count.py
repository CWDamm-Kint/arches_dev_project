from arches.app.models.graph import Graph
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile
from arches.app.models.models import Value

from django.http import HttpResponse
from django.http import JsonResponse

def create_day_count(request):

    tiles_qs = Tile.objects.all()
    values_qs = Value.objects.all()

    count_dict = {}

    for tile in tiles_qs:
        if str(tile.nodegroup_id) == "0a3afb72-6ec0-11ef-8309-5b5a59d59ccc": # all the parking attribute nodegroups
            for value in tile.data['78532bad-6ec0-11ef-8309-5b5a59d59ccc']: # create list of parking values
                if value not in count_dict:
                    count_dict[value] = 1
                else:
                    count_dict[value] += 1
            pass

    value_lu = {} # create lookup for parking value ids

    for value in values_qs:
        value_lu[str(value.valueid)] = value.value
  
    results_dict = {} # combine into results dictionary
    
    for value in count_dict:
        value_name = value_lu[value]
        results_dict[value_name] = count_dict[value]

    print(results_dict)

    return JsonResponse(results_dict)

    