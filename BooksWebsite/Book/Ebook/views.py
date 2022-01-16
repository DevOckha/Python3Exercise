from io import RawIOBase
from django.shortcuts import render
from .models import Book, Category


def index(request):
    context = {
        'books':Book.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'Ebook/index.html', context)

def detail(request, id):
    book_detail = Book.objects.get(id = id)
    return render(request, 'Ebook/detail.html', {'book_detail': book_detail})