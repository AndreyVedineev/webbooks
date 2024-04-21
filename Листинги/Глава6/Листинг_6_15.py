from django.template.response import TemplateResponse


def index(request):
    header = "Иностранные языки"  # символьная переменная
    list_langs = ["Английский", "Немецкий", "Испанский",
                  "Французский", "Итальянский"]  # список
    data = {"header": header, "list_langs": list_langs}
    return TemplateResponse(request, "firstapp/index_app1.html", data)
