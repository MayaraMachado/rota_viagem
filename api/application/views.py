from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.route_domain import RouteDomain
from .serializers import RouteInsertSerializer, BestPathSerializer

class RouteView(APIView):
    """
    """
    def __init__(self):
        self.domain = RouteDomain()

    def get(self, request):
        '''
        '''
        from_route = self.request.query_params.get('from')
        to_route = self.request.query_params.get('to')

        route, total_cost = self.domain.best_path(from_route, to_route)
        response = BestPathSerializer({'route':route, 'total_cost':total_cost})
        return Response(response.data, status=status.HTTP_200_OK)

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
            sucess = self.domain.insert(**serializer.validated_data)
            if sucess:
                return Response(status=status.HTTP_201_CREATED)
        return Response({"message":"Oops! Something bad happened, please try again later!"}, status=status.HTTP_400_BAD_REQUEST)
