from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views import generic
from urllib import request
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator

from catalog.models import Author, Book, BookInstance


def index(request):
    text_head = "На нашем сайте вы можете получить книги в электронном виде"
    books = Book.objects.all()
    num_books = Book.objects.all().count
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    authors = Author.objects
    num_authors = Author.objects.count
    # Количество посещений этого view, подсчитанное в переменной session
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "text_head": text_head,
        "books": books,
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "authors": authors,
        "num_authors": num_authors,
        "text_body": "Это содержимое главной страницы сайта",
        "num_visits": num_visits,
    }

    return render(request, "catalog/index.html", context)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"


class AuthorListView(ListView):
    model = Author
    paginate_by = 4


class AuthorDetailView(DetailView):
    model = Author


def about(request):
    text_head = "Сведения о компании"
    name = "ООО A_Vedineev"
    rab1 = "Разработка приложений"
    rab2 = "Продажа цветов"
    rab3 = (
        "Создание графических АРТ-объектов на основе"
        " систем искусственного интеллекта"
    )
    rab4 = (
        "Создание цифровых интерактивных книг, учебных пособий"
        " автоматизированных обучающих систем"
    )
    context = {
        "text_head": text_head,
        "name": name,
        "rab1": rab1,
        "rab2": rab2,
        "rab3": rab3,
        "rab4": rab4,
    }
    # передача словаря context с данными в шаблон
    return render(request, "catalog/about.html", context)


def contact(request):
    text_head = "Контакты"
    name = 'ООО "A_Vedineev"'
    address = "Краснодарский край, пгт. Мостовской, ул. Горького 144"
    tel = "+7918 024 13 03"
    email = "avedineev@yandex.ru"
    # Словарь для передачи данных в шаблон index.html
    context = {
        "text_head": text_head,
        "name": name,
        "address": address,
        "tel": tel,
        "email": email,
    }
    # передача словаря context с данными в шаблон
    return render(request, "catalog/contact.html", context)


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="2")
            .order_by("due_back")
        )
