from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def hai(request):
    News = Post.objects.all()
    return render(request,'News/index.html',{'News':News})

