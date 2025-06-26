from django.shortcuts import render
from .models import *
# Create your views here.
def home_view(request): 
    posts = Post.objects.all() # this has all the objects of posts i.e all images
    # down below we have key value pair i.e posts key and has this posts list to its value ,its like passing data
    # to html
    return render(request,'a_posts/home.html',{'posts': posts})

def post_create_view(request):
    return render(request,'a_posts/post_create.html')