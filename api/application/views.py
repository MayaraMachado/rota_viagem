from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from api.domain.route_domain import RouteDomain
from .serializers import RouteInsertSerializer, BestPathSerializer

class RouteView(APIView):
    """
    """
    def __init__(self):
        self.domain = RouteDomain(settings.FILE_EXAMPLE)

    def get(self, request):
        '''
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
            {
                "origin" : "GRU",
                "end"    : "DSL",
                "cost"   : 49
            }
        '''
    
        serializer = RouteInsertSerializer(data=request.data)
        if serializer.is_valid():
            try:
                sucess = self.domain.insert(**serializer.validated_data)
                return Response(status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"message" : "Invalid route attributes."}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
