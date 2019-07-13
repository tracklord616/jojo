from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .models import Post


def post_list(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'Posts': posts})
def user_posts(request,user)
    user = user.objects.get(username=user)
    posts = post.object.all().filter(author = user)
    return render(request,{posts : posts})
