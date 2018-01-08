from django.shortcuts import render

from blogging.models import Post


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