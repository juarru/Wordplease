"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from blogging.views import Home, PostDetail, NewPostView, AuthorPostView
from bloggers.views import LoginView, logout, AuthorView, SignUpView

from rest_framework.authtoken import views
from bloggers.api import AuthorAPI, AuthorDetailAPI
from blogging.api import BlogListAPI, BlogAuthorListAPI, PostsListAPI, PostDetailAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('blogs/', AuthorView.as_view(), name='blogs_page'),
    path('blogs/<slug:username>', AuthorPostView.as_view(), name="blog_author_page"),
    path('blogs/<slug:username>/<int:pk>', PostDetail.as_view(), name="post_detail_route"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', logout, name="logout"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('new-post', NewPostView.as_view(), name="newpost"),

    # API
    path('api/1.0/authors/get-token/', views.obtain_auth_token, name="token_api"),
    path('api/1.0/authors/', AuthorAPI.as_view(), name='author_api'),
    path('api/1.0/authors/<slug:pk>', AuthorDetailAPI.as_view(), name="author_detail_api"),

    path('api/1.0/blogs/', BlogListAPI.as_view(), name="blogs_list_api"),
    path('api/1.0/blogs/<slug:username>', BlogAuthorListAPI.as_view(), name="author_blogs_list_api"),

    path('api/1.0/posts/', PostsListAPI.as_view(), name="post_list_api"),
    path('api/1.0/posts/<int:pk>', PostDetailAPI.as_view(), name="post_detail_api"),

]
