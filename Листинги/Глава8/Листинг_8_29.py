# Загрузка  видео файлов
class VideoFile(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Описание файла",)
    file = models.FileField(upload_to='videos',
                            verbose_name="Видео файл",
                            null=True, blank=True)
    obj_video = models.Manager()

    def __str__(self):
        return self.title
