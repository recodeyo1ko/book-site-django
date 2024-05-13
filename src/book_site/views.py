from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Create your views here.

def home(request):
    return render(request, 'home/top.html')

def book_index(request):
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'books/index.html', {'books': books, 'form': form})

def book_show(request):
    return render(request, 'books/show.html')


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    books = Book.objects.all()
    form = BookForm()
    return render(request, 'books/index.html', {'books': books, 'form': form})