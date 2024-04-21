# авторы
class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Введите имя автора",
                                  verbose_name="Имя автора")
    last_name = models.CharField(max_length=100,
                                 help_text="Введите фамилию автора",
                                 verbose_name="Фамилия автора")
    date_of_birth = models.DateField(
        help_text="Введите дату рождения",
        verbose_name="Дата рождения",
        null=True, blank=True)
    about = models.TextField(help_text="Введите сведения об авторе",
                             verbose_name="Сведения об авторе")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите фото автора",
                              verbose_name="Фото автора",
                              null=True, blank=True)

    def __str__(self):
        return self.last_name
