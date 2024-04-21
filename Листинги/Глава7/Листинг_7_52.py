from django.http import HttpResponse
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
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse(
                "<h2>Имя введено коррректно – {0} </h2 > ".format(name))
        else:
            return HttpResponse("Ошибка ввода данных")
    else:
        userform = UserForm()
        return render(request,
                      "firstapp/my_form.html", {"form": userform})
