"""View module for handling requests about posts"""
from datetime import date
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.db.models import Q
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
        today = date.today()
        posts = Post.objects.filter(approved=True, publication_date__lte=today).order_by('publication_date')
        # Q(user=request.auth.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of posts
        """
        
    @action(methods=["get"], detail=False)
    def my_posts(self, request):
        today = date.today()
        user = RareUser.objects.get(user=request.auth.user)
        # (user on the left side is the property on Post you are referring to, 
        # user on the right is the one you just defined that you want to compare it to)
        posts = Post.objects.filter(user=user).order_by('publication_date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
        
    def create(self, request):
        
        """Handle POST operations

        Returns:
            Response -- JSON serialized game review instance
        """
        author = RareUser.objects.get(user=request.auth.user)
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
        
class CreatePostSerializer(serializers.ModelSerializer):
    """JSON serializer for creating game reviews
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date', 'image_url', 'content', 'approved', 'category' 
        )
        
        # Define DELETE request function for deleting posts
        
        # Define PUT request function for editing posts
        