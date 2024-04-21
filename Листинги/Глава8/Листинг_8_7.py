from .forms import UserForm
from django.shortcuts import render, redirect
from .models import Person


def index(request):
    my_text = 'Изучаем модели Django'
    people_kol = Person.object_person.count()
    context = {'my_text': my_text, "people_kol": people_kol}
    return render(request, "firstapp/index.html", context)


def about(request):
    return render(request, "firstapp/about.html")


def contact(request):
    return render(request, "firstapp/contact.html")


# взаимодействие с формой ввода данных о клиентах
def my_form(request):
    if request.method == "POST":  # пользователь отправил данные
        form = UserForm(request.POST)  # создание экземпляра формы
        if form.is_valid():  # проверка валидности формы
            form.save()  # запись данных в БД
            # остаемся на той же странице, обновляем форму

    # Загрузить форму для ввода клиентов
    my_text = 'Сведения о клиентах'
    people = Person.object_person.all()
    form = UserForm()
    context = {'my_text': my_text, "people": people, "form": form}
    return render(request, "firstapp/my_form.html", context)
