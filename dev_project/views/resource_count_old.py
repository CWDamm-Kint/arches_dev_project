import sys 
sys.path.append("../arches")

from arches.app.models.graph import Graph
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile
from arches.app.models.models import Value

import json
import uuid
from django.http import JsonResponse, HttpResponse
from arches.settings import SYSTEM_SETTINGS_RESOURCE_ID

def create_resource_count(request):
    
    graph_qs = Graph.objects.all()
    resources_qs = Resource.objects.all()

    system_resource_id = str(Resource.objects.filter(pk=uuid.UUID(SYSTEM_SETTINGS_RESOURCE_ID))[0].graph_id)
    # print("\nSYSTEM RESOURCE", system_resource_id)

    resource_graphs_lu = {} # identify all resource models

    for graph in graph_qs:
        if graph.isresource == True and (str(graph.graphid) != system_resource_id):
            resource_graphs_lu[str(graph.graphid)] = graph.name
            print(graph.name, graph.graphid)

    # print("\n", "RESOURCE GRAPHS LOOKUP", resource_graphs_lu)

    resource_counts = {} # create dictionary where all counts for these models are zero

    for graph in graph_qs:
        if graph.isresource == True and (str(graph.graphid) != system_resource_id):
            resource_counts[str(graph.graphid)] = 0

    # print("\n",  "RESOURCE GRAPHS COUNTS",  resource_counts)

    for resource in resources_qs: # loop through resources, adding to count dictionary
        print("\n", vars(resource))
        if str(resource.graph_id) in resource_counts:
            resource_counts[str(resource.graph_id)] += 1

    # print("\n",  "RESOURCE GRAPHS COUNTS UPDATED",  resource_counts)

    resource_counts_with_names = {} # combine names and counts in final dictionary

    for graph in resource_counts:
        resource_counts_with_names[resource_graphs_lu[graph]] = resource_counts[graph]

    # print("\n",  "FINAL DICT",  resource_counts_with_names)

    filtered_dict = {} # filter out zero values

    for resource, count in resource_counts_with_names.items():
        if count != 0:
            filtered_dict[resource] = count

    # print("\n",  "FINAL DICT FILTERED",  filtered_dict)

    json_object = json.dumps(resource_counts_with_names) 

    return JsonResponse(filtered_dict, json_dumps_params={'indent': 4})

    # return HttpResponse("Hello world")
