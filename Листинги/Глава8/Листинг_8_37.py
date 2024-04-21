# импорт модели и формы для работы с аудио файлами
from .models import AudioFile
from .forms import AudioForm


# загрузка аудио файлов
def form_up_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загруженные аудио файлы'
    form = AudioForm()
    file_obj = AudioFile.obj_audio.all()
    context = {'my_text': my_text, "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_audio.html', context)


# удаление аудио файлов из БД
def delete_audio(request, id):
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
