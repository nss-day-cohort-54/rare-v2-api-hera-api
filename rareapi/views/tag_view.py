"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag


class TagView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized game type
        """
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)


def list(self, request):
    """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of game types
        """
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')