from django.core.management.base import BaseCommand, CommandError
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile
from arches.app.models.models import Value

class Command(BaseCommand):

    def handle(self, *args, **options):
        resource_qs = Resource.objects.all()

        # for resource in resource_qs: # modify all tiles with a certain postcode by iterating through the resources
        #     resource.load_tiles()
        #     for tile in resource.tiles: 
        #         if str(tile.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc': 
        #             if(tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="NW3 5PZ"):
        #                 tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"] = "I've been replaced"
        #                 tile.save()
        #                 print("\n", vars(tile))  
        #                 pass

        for resource in resource_qs: # check for the replaced postcodes
            resource.load_tiles()
            for tile in resource.tiles: 
                if str(tile.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc': 
                    if(tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="I've been replaced"):
                        # print(tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"])
                        pass

        t_qs = Tile.objects.all() 

        # for tile in t_qs: 
        #     if str(tile.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc' and tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="I've been replaced": 
        #         tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"] = "NW3 5PZ"
        #         tile.save()
        #         print("\n", vars(tile))  
        #         pass

        for tile in t_qs: # change them back
            if str(tile.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc' and tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"]=="NW3 5PZ": 
                # print("\n", vars(tile))  
                pass

        
        for resource in resource_qs: # check for the replaced postcodes
            resource.load_tiles()
            
            change_coords = False

            for tile in resource.tiles: 
                if (str(tile.nodegroup_id) == '29e54f3c-6ebf-11ef-8309-5b5a59d59ccc' and 
                    tile.data["3cf0a734-6ebf-11ef-8309-5b5a59d59ccc"].startswith("NW1")): 
                    change_coords = True
                    break
             
            if change_coords == True:

                for tile in resource.tiles: 
                    if str(tile.nodegroup_id) == '08803190-6ebf-11ef-8309-5b5a59d59ccc':
                        lat = tile.data['778b8936-6ebf-11ef-8309-5b5a59d59ccc']['features'][0]['geometry']['coordinates'][0]
                        long = tile.data['778b8936-6ebf-11ef-8309-5b5a59d59ccc']['features'][0]['geometry']['coordinates'][1]

                        tile.data['778b8936-6ebf-11ef-8309-5b5a59d59ccc']['features'][0]['geometry']['coordinates'][0] = long
                        tile.data['778b8936-6ebf-11ef-8309-5b5a59d59ccc']['features'][0]['geometry']['coordinates'][1] = lat
                
                        tile.save()

                for tile in resource.tiles: 
                    if str(tile.nodegroup_id) == '08803190-6ebf-11ef-8309-5b5a59d59ccc' and change_coords == True:
                        print(tile.data['778b8936-6ebf-11ef-8309-5b5a59d59ccc']['features'][0]['geometry']['coordinates'][0],
                            tile.data['778b8936-6ebf-11ef-8309-5b5a59d59ccc']['features'][0]['geometry']['coordinates'][1])
