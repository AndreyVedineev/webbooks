# импорт для добавления автора
from .forms import Form_add_author
from django.urls import reverse


# Создание нового автора в БД
def add_author(request):
    if request.method == 'POST':
        form = Form_add_author(request.POST, request.FILES)
        if form.is_valid():
            # получить данные из формы
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            date_of_birth = form.cleaned_data.get("date_of_birth")
            about = form.cleaned_data.get("about")
            photo = form.cleaned_data.get("photo")
            # создать объект для записи в БД
            obj = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                about=about,
                photo=photo)
            # сохранить полученные данные
            obj.save()
            # загрузить страницу со списком автором
            return HttpResponseRedirect(reverse('authors-list'))
    else:
        form = Form_add_author()
        context = {"form": form}
        return render(request, "catalog/authors_add.html", context)
