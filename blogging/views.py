from django.shortcuts import render

from blogging.models import Post


def home(request):
    latest_posts = Post.objects.all().order_by("-release_date")
    context = {'posts': latest_posts[:5]}
    return render(request, "home.html", context)