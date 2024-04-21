from django.template.response import TemplateResponse

def index(request):
    header = "Персональные данные"                  # символьная переменная
    langs = ["Английский", "Немецкий", "Испанский"] # список
    user = {"name": "Максим,", "age": 30}           # словарь
    addr = ("Виноградная", 23, 45)                  # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "index.html", data)
