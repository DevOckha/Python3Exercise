from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'blog/index.html')



def blogs(request):
    return render(request, 'blog/blogs.html')



def blogs_detail(request, id):
    return render(request, 'blog/blogs_detail.html', {'id':id})