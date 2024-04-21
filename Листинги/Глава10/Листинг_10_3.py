from django.shortcuts import render


def index(request):
    # Словарь для передачи данных в шаблон
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)
