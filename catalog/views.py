from django.shortcuts import render


from django.http import HttpResponse

from catalog.models import Author, Book, BookInstance


def index(request):
    text_head = "На нашем сайте вы можете nолучить книги в электронном виде"
    books = Book.objects.all()
    num_books = Book.objects.all().count
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status_exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count
    context = {
        'text_head': text_head,
        "books": books,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "authors": authors,
        "num_authors": num_authors,
        'text_body': "Это содержимое главной страницы сайта",
    }

    return render(request, "catalog/index.html", context)
