from .models import Book, Author, BookInstance


class AuthorListView(ListView):
    model = Author
    paginate_by = 4
