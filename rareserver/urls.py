"""rareserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from rareapi.views import TagView
from django.urls import path
from rareapi.views import register_user, login_user
from rareapi.views.category import CategoryView
from rareapi.views.comment import CommentView
from rareapi.views.post import PostView
from rareapi.views.post_tag import PostTagView
from rareapi.views.rare_user_view import RareUserView


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'categories', CategoryView, 'category')
router.register(r'posts', PostView, 'post')
router.register(r'posttags', PostTagView, 'posttag')
router.register(r'tags', TagView, 'tag')
router.register(r'comments', CommentView, 'comment')

router.register(r'users', RareUserView, 'rareuser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
