from rest_framework import serializers


class BestPathSerializer(serializers.Serializer):
    route      = serializers.CharField()
    total_cost = serializers.IntegerField()

class RouteInsertSerializer(serializers.Serializer):
    origin =  serializers.CharField()
    end    =  serializers.CharField()
    cost   =  serializers.IntegerField()