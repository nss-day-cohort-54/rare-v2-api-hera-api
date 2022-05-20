"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTag


class PostTagView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        post_tag = PostTag.objects.get(pk=pk)
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        post_tag = PostTag.objects.all()
        serializer = PostTagSerializer(post_tag, many=True)
        return Response(serializer.data)
    
class PostTagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = PostTag
        fields = ('id', 'tag', 'post')
        depth = 1