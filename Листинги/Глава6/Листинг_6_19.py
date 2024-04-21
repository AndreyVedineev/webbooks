from django.template.response import TemplateResponse
import datetime


def index(request):
    header = "Фильтры в шаблонах"
    value_num = 2
    value_date = datetime.datetime.now()
    value_time = datetime.datetime.now()
    value_title = "это пример использования фильтров"
    value_upper = "это строка в верхнем регистре"
    data = {"header": header, "value_num": value_num, "value_date": value_date,
            "value_time": value_time, "value_title": value_title,
            "value_upper": value_upper}
    return TemplateResponse(request, "firstapp/index_app1.html", data)
