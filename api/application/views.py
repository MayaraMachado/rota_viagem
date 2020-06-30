from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from api.domain.route_domain import RouteDomain
from .serializers import RouteInsertSerializer, BestPathSerializer

class RouteView(APIView):
    """
        This is the Route view. It is responsible for handling de 
        API requests, and to redirect to the domain class responsible.
    """
    def __init__(self):
        '''
            For development purposes, this View always instantiates RotaDomain 
            with the .csv file indicated in the challenge statement.

            If it is desired to use a .txt file instead, it will be necessary 
            to change the file name in the project settings (bexs_desafio / settings.py)
        '''
        self.domain = RouteDomain(settings.FILE_EXAMPLE)

    def get(self, request):
        '''
            The Get method queries the best route to reach a destination from a point, the 
            application uses the values ​​informed in the consumption .txt or .csv file and 
            returns the result found.
            This method will always receive two queryparams: to and from. These params will 
            define the origin and destination for the best path query.        
        '''     
        try:
            from_route = self.request.query_params.get('from').upper()
            to_route = self.request.query_params.get('to').upper()
            route, total_cost = self.domain.best_path(from_route, to_route)
            response = BestPathSerializer({'route':route, 'total_cost':total_cost})
            return Response(response.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"message" : 'The nodes are not connected.'},status=status.HTTP_400_BAD_REQUEST)
        except AttributeError as e:
            print(e)
            return Response({"message" : "Please, send two valid locations to verify: origin and destination."},status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        '''
            The post method allows one more connection to be added to the .txt or .csv file used. 
            It is an analogy with the persistence functionality in a database.
            
            Requests must be in the following format:

                {
                    "origin" : "GRU",
                    "end"    : "DSL",
                    "cost"   : 49
                }
        '''
    
        serializer = RouteInsertSerializer(data=request.data)
        if serializer.is_valid():
            try:
                sucess = self.domain.insert(serializer.validated_data['routes'])
                return Response(status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"message" : "Invalid route attributes."}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
