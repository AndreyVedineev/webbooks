from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
