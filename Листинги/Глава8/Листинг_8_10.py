from .forms import UserForm
from django.shortcuts import render, redirect
from .models import Person
from django.http import HttpResponseNotFound


# изменение данных о клиенте в БД
def edit_form(request, id):
    person = Person.object_person.get(id=id)
    # Если пользователь вернул отредактированные данные
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('my_form')

    # Если пользователь отправляет данные на редактирование
    data = {"person": person}
    return render(request, "firstapp/edit_form.html", context=data)


# удаление данных о клиенте из БД
def delete(request, id):
    try:
        person = Person.object_person.get(id=id)
        person.delete()
        return redirect('my_form')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
