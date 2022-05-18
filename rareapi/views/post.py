"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from rareapi.models import Post
from rareapi.models import RareUser
from django.contrib.auth.models import User


# MAKE SURE THERE IS A POST VIEWSET IN THE rareserver/urls.py

class PostView(ViewSet):
    """post views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single post"""
        
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
        """Returns:
            Response -- JSON serialized post
        """
    
    
    def list(self, request):
        """Handle GET requests to get all posts"""
        
        posts = Post.objects.filter(approved=True).order_by('publication_date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of posts
        """
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
         

        
class RareUserSerializer(serializers.ModelSerializer):
    user= UserSerializer() 
    class Meta:
        model = RareUser
        fields = ('id', 'bio', 'user')
              
        
class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    user= RareUserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date', 'image_url', 'content', 'approved', 
                  'category', 'user')
        depth = 2      
        
        
        
        # Define POST request function for creating posts
        # Add CreatePostSerializer
        
        # Define DELETE request function for deleting posts
        
        # Define PUT request function for editing posts
        