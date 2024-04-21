# импорт модели и формы для работы с файлами
from .models import File
from .forms import FileForm


# загрузка файлов pdf
def form_up_pdf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загруженные файлы'
    form = FileForm()
    file_obj = File.objects.all()
    context = {'my_text': my_text, "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_pdf.html', context)


# удаление файлов из БД
def delete_pdf(request, id):
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
