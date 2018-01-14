from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from blogging.forms import PostForm
from blogging.models import Post
from django.contrib import messages

import datetime
from django.utils import timezone

class Home(ListView):
    model = Post
    template_name = "home.html"

    def get_queryset(self):
        # now = datetime.datetime.now()
        now = timezone.now()
        queryset = super(Home, self).get_queryset()
        return queryset.filter(release_date__lte=now.strftime("%Y-%m-%d")).order_by('-release_date')

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_queryset(self):
        # now = datetime.datetime.now()
        now = timezone.now()
        queryset = super(PostDetail, self).get_queryset()
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username__iexact=username)
        return queryset.filter(author=user, release_date__lte=now.strftime("%Y-%m-%d")).order_by('-release_date')

class NewPostView(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})

    def post(self, request):
        post = Post()
        post.author = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_route", args=[post.author.username,post.pk])
            message = "Post created successfully"
            message += '<a href="{0}"> - View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})

class AuthorPostView(ListView):
    model = Post
    template_name = "author_posts.html"

    def get_queryset(self):
        # now = datetime.datetime.now()
        now = timezone.now()
        queryset = super(AuthorPostView, self).get_queryset()
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username__iexact=username)
        return queryset.filter(author=user, release_date__lte=now.strftime("%Y-%m-%d")).order_by('-release_date')

    def get_context_data(self, **kwargs):
        username = self.kwargs.get("username")
        context = super().get_context_data(**kwargs)
        context['username'] = username
        return context