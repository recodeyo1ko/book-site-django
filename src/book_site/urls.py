from django.urls import path
from . import views
from .views import book_create
from .views import book_delete

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_index, name='book_index'),
    path('books/<int:book_id>/', views.book_show, name='book_show'),
    path('books/<int:book_id>/delete/', book_delete, name='book_delete'),
    path('books/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('books/create/', book_create, name='book_create'),
]