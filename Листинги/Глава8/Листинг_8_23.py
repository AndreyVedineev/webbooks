# Загрузка  файлов
class File(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Описание файла",)
    file = models.FileField(upload_to='files',
                            verbose_name="Файл PDF",
                            null=True, blank=True)

    def __str__(self):
        return self.title
