"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User

from rareapi.models.rare_user import RareUser


class RareUserView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        rareuser = RareUser.objects.get(pk=pk)
        serializer = RareUserSerializer(rareuser)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        rareusers = RareUser.objects.all()
        serializer = RareUserSerializer(rareusers, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email' )

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    user = UserSerializer()
    class Meta:
        model = RareUser
        fields = ('id', 'bio', 'profile_image_url', 'user' )
        depth = 2