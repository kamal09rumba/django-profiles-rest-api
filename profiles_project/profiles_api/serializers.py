from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serializes a namefield to test APIView """
    name = serializers.CharField(max_length=10)