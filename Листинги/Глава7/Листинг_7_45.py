from django.shortcuts import render
from .forms import UserForm


def index(request):
    my_text = 'Изучаем формы Django'
    context = {'my_text': my_text}
    return render(request, "firstapp/index.html", context)


def about(request):
    return render(request, "firstapp/about.html")


def contact(request):
    return render(request, "firstapp/contact.html")


def my_form(request):
    my_form = UserForm(field_order=["age", "name"])
    context = {"form": my_form}
    return render(request, "firstapp/my_form.html", context)
