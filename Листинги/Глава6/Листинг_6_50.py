def index(request):
    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
             'IV квартал->']
    my_month = ['Январь', 'Февраль', 'Март',
               'Апрель', 'Май', 'Июнь',
               'Июль', 'Август', 'Сентябрь',
               'Октябрь', 'Ноябрь', 'Декабрь']
    context = {'my_month': my_month, 'my_kv': my_kv}
    return render(request, "firstapp/index.html", context)
