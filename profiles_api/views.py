from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View """
    serializer_class = serializers.HelloSerializer
    # jobserializer_class = serializers.JobSerializer

    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            'Uses HTTP function (get, postst patch, push, delete)',
            'Its similer to traditional Django View',
            'Gives you more control over your application logic',
            'is mapped manually to URL'
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)
        # jobseriallizer = self.jobserializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            #job = jobseriallizer.get("job")
            message = f'Hi,I am {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message':'PUT'})

    def patch(self, request, pk=None):
        """Handle the partial updating an object"""
        return Response({'message':'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message':'Delete'})
