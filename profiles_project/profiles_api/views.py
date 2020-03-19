from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from .models import UserProfile
from .permissions import UpdateOwnProfile

class HelloApiView(APIView):
    # Test API view

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Returns a list of APIView features
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your aplication logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Ola k ase', 'an_apiview': an_apiview})

    def post(self, request):
        # Create a hello message with our name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Ola k ase {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        # Handle updating an object
        return Response({'method': 'PUT'})

    def delete(self, request, pk=None):
        # Delete an object
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    # Test API Viewset

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # Return hello message
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Ola k ase', 'a_viewset': a_viewset})

    def create(self, request):
        # Create a new hello message
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Ola k ase {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        # Handle gettin an object by its id
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        # Handle updating an object
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        # Handle updating part of an object
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        # Hanlde removing an object
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    # Handle creating and updating profiles
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
