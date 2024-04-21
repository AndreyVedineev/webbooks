def index(request):
    # return render(request, "firstapp/home.html")
    data = {"header": "Передача параметров в шаблон Django",
           "message":
           "Загружен шаблон templates/firstapp/index_app1.html"}
    return render(request, "firstapp/index_app1.html", context=data)
