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

def book_show(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/show.html' , {'book': book})

def book_edit(request):
    return render(request, 'books/edit.html' )

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

def book_show(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/show.html', {'book': book})

def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_index')

def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_show', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit.html', {'form': form})