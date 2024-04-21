from .models import Book, Author, BookInstance
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
