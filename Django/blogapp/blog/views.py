from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog,Category


def index(request):
    context = {
        'blogs':Blog.objects.filter(is_active=True, is_home=True),
        'categories':Category.objects.all()
    }
    return render(request, 'blog/index.html', context)


def blogs(request):
    context = {
        'blogs':Blog.objects.filter(is_active=True),
        'categories':Category.objects.all()

    }
    return render(request, 'blog/blogs.html', context)


def blogs_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blogs_details.html', {
        'blog': blog
    })