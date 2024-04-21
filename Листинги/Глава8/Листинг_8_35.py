# Загрузка  аудио файлов
class AudioFile(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Описание файла",)
    file = models.FileField(upload_to='audios',
                            verbose_name="Аудио файл",
                            null=True, blank=True)
    obj_audio = models.Manager()

    def __str__(self):
        return self.title
