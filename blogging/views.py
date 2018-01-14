from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from blogging.forms import PostForm
from blogging.models import Post
from django.contrib import messages


def home(request):
    latest_posts = Post.objects.all().order_by("-release_date")
    context = {'posts': latest_posts[:5]}
    return render(request, "home.html", context)

def post_detail(request, pk):
    target_post = Post.objects.filter(pk=pk)#.select_related("category")
    if len(target_post) == 0:
        return render(request, "404.html", status=404)
    else:
        post = target_post[0]
        context = {'post': post}
        return render(request, "post_detail.html", context)

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
            url = reverse("post_detail_route", args=[post.pk])
            message = "Post created successfully"
            message += '<a href="{0}"> - View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})