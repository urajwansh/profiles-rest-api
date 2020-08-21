from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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
        return Response({'message':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API VIewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to url using routing',
            'Provides more functionality with less code'
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """Create anew hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})
