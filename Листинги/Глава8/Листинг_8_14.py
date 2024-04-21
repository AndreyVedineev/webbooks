# Загрузка изображений
class Image(models.Model):
    title = models.CharField(max_length=100, null=False,
                             verbose_name="Описание изображения",)
    image = models.ImageField(upload_to='images',
                              verbose_name="Файл с изображением",
                              null=True, blank=True)
    obj_img = models.Manager()

    def __str__(self):
        return self.title
