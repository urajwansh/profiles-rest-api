from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


# class JobSerializer(serializers.Serializer):
#     """Serializes the job profile inserted"""
#     job = serializers.CharField(max_length = 10)
