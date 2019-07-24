from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def index(request): 
    anonyPost = Post.objects.all

    return render(request, 'anonymousBoard/index.html',{
        'posts': anonyPost,
    })