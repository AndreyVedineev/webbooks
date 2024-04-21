from django.template.response import TemplateResponse

def index(request):
    header = "Разветвления в шаблонах"
    num = 1
    var1 = "Это первая ветка в инструкции if"
    var2 = "Это вторая ветка в инструкции if"
    data = {"header": header, "num": num, "var1": var1, "var2": var2}
    return TemplateResponse(request, "firstapp/index_app1.html", data)
