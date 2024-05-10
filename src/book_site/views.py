from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/top.html')

def book_index(request):
    return render(request, 'books/index.html')

def book_show(request):
    return render(request, 'books/show.html')