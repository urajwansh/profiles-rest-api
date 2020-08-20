from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View """

    def get(self, request, format=None):
        """Returns a list of APIView feature"""
        an_apiview = [
            'Uses HTTP function (get, postst patch, push, delete)',
            'Its similer to traditional Django View',
            'Gives you more control over your application logic',
            'is mapped manually to URL'
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
        
