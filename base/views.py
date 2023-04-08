from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html', {'posts': posts})

def post(request, id= None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if(id is None):
            Post.objects.create(
                title = request.POST.get('title'),
                text = request.POST.get('title')
            )
        else:
            p=Post.objects.get(id = id)
            p.title = request.POST.get('title')
            p.text = request.POST.get('title')
            p.save()

    context ={}
    if id is not None:
        p = Post.objects.get(id = id)
        context['post'] = p
    return render(request, 'post.html', context)
