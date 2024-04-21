# Импорт для редактирования книг
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


# Класс для создания в БД новой записи о книге
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('edit_books')


# Класс для обновления в БД  записи о книге
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('edit_books')


# Класс для удаления из БД  записи о книге
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('edit_books')
