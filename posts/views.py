# from django.shortcuts import render
# from . import models

# def post_list(request):
#     posts = models.Post.objects.all()
#     return render(request, 'post_list.html', {'posts': posts})

from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'