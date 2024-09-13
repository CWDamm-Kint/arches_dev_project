import sys 
sys.path.append("../arches")

from arches.app.models.graph import Graph
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile
from arches.app.models.models import Value

import uuid
from django.http import JsonResponse, HttpResponse
from arches.settings import SYSTEM_SETTINGS_RESOURCE_ID

def create_resource_count(request):
    
    graph_qs = Graph.objects.all()
    resources_qs = Resource.objects.all()

    system_resource_id = str(Resource.objects.filter(pk=uuid.UUID(SYSTEM_SETTINGS_RESOURCE_ID))[0].graph_id)

    resource_graphs_lu = {} # identify all resource model names and exclude system settings

    for graph in graph_qs:
        if graph.isresource == True and (str(graph.graphid) != system_resource_id):
            resource_graphs_lu[str(graph.graphid)] = graph.name

    print("\n", "RESOURCE GRAPHS LOOKUP", resource_graphs_lu)

    resource_counts = {}  # loop through resources, if it's in the graph lookup, then either create, or increment, its entry within resource counts

    for resource in resources_qs:
        
        if str(resource.graph_id) in resource_graphs_lu:
            graph_name = resource_graphs_lu[str(resource.graph_id)]

            if graph_name in resource_counts:
                resource_counts[graph_name] += 1
                
            else:
                resource_counts[graph_name] = 1

    print("\n",  "RESOURCE GRAPHS COUNTS UPDATED",  resource_counts)

    return JsonResponse(resource_counts, json_dumps_params={'indent': 4})

    # return HttpResponse("Hello world")

