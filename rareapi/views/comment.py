"""View module for handling requests about comments"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.comment import Comment
from rareapi.models.rare_user import RareUser


class CommentView(ViewSet):
    """"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized game type
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of game types
        """
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """

        rareuser = RareUser.objects.get(user=request.auth.user)
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(rareuser=rareuser)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_on',)
        depth = 1


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']
