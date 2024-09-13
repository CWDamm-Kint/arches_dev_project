from django.core.management.base import BaseCommand, CommandError
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile
from arches.app.models.models import Value

class Command(BaseCommand):

    def handle(self, *args, **options):
        r_qs = Resource.objects.all()
        # print(r_qs)

        for r in r_qs: # all tiles with a certain postcode by iterating through the resources
            r.load_tiles()
            for t in r.tiles: 
                if str(t.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc': 
                    if(t.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="NW3 5PZ"):
                        # print("\n", vars(t))  
                        pass
                    
        t_qs = Tile.objects.all() # list all the tiles in the database   

        for t in t_qs: # all tiles with a certain postcode by iterating through the tiles  
            if str(t.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc' and t.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="NW3 5PZ": 
                # print("\n", vars(t))  
                pass

        at_any_time_concept = Value.objects.filter(value="at any time")
        at_any_time_valueid = str(at_any_time_concept[0].valueid) # find value id for 'at any time' concept
        at_any_time_count = 0

        for t in t_qs: # find open any time tiles
            if str(t.nodegroup_id) == "0a3afb72-6ec0-11ef-8309-5b5a59d59ccc" and at_any_time_valueid in t.data["78532bad-6ec0-11ef-8309-5b5a59d59ccc"]:
                #  print("\n", vars(t))
                #  print("\n", t.data["78532bad-6ec0-11ef-8309-5b5a59d59ccc"])
                 at_any_time_count += 1
                 pass

        # print(at_any_time_count) # count of open at any time

        mon_sat_concept = Value.objects.filter(value="mon-sat")
        mon_sat_valueid = str(mon_sat_concept[0].valueid) # find value id for 'mon-sat' concept       

        for r in r_qs: # all tiles with a certain postcode and open any time by iterating through the resources
            r.load_tiles()
            open_mon_sat = False
            postcode_matches = False
            
            for t in r.tiles: 
                if str(t.nodegroup_id) == "0a3afb72-6ec0-11ef-8309-5b5a59d59ccc" and mon_sat_valueid in t.data["78532bad-6ec0-11ef-8309-5b5a59d59ccc"]:
                    open_mon_sat = True
                if str(t.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc' and t.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="NW3 7EH": 
                    postcode_matches = True
            
            if  postcode_matches and open_mon_sat:
                print("\n", vars(r))

        # carpark = Resource.objects.filter(pk="75f15773-cdc1-47cb-ae72-3eb6ff3e74c4")[0] # select a resource and view it's vars and tiles
        # carpark.load_tiles() # 
        # print("CARPARK RESOURCE", vars(carpark))
        # for t in carpark.tiles: 
        #     print(vars(t))

        # print("NAME TILE", vars(carpark.tiles[1]))


        # print("HERE", t_qs.count())

        # maple_street_name = Tile.objects.filter(pk="f91e5bd4-512f-4c3e-8825-587310da9fb8")

        # print("HERE", vars(maple_street_name[0]))
