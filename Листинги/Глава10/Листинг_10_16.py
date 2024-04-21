class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3
