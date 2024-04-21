from django.http import HttpResponse, \
    HttpResponsePermanentRedirect, \
    HttpResponseRedirect


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponseRedirect("/about")
    # return HttpResponse("<h2>Контакты</h2>")


def products(request, productid=1):
    category = request.GET.get("cat", "Не задана")
    output = "<h2>Продукт № {0}  Категория: {1}</h2>"\
        .format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get("name", "Не задано")
    output = "<h2>Пользователь</h2> <h3>id: {0}  Имя: {1}</h3 >"\
        .format(id, name)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect("/")
