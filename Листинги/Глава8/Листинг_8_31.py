# импорт модели и формы для работы с видео файлами
from .models import VideoFile
from .forms import VideoForm


# загрузка видео файлов
def form_up_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загруженные видео файлы'
    form = VideoForm()
    file_obj = VideoFile.obj_video.all()
    context = {'my_text': my_text, "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_video.html', context)


# удаление видео файлов из БД
def delete_video(request, id):
    try:
        video = VideoFile.obj_video.get(id=id)
        video.delete()
        return redirect('form_up_video')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
