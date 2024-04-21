# книги
class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Введите название книги",
                             verbose_name="Название книги")
    genre = models.ForeignKey('Genre',
                              on_delete=models.CASCADE,
                              help_text=" Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    publisher = models.ForeignKey('Publisher',
                                  on_delete=models.CASCADE,
                                  help_text="Выберите издательство",
                                  verbose_name="Издательство", null=True)
    year = models.CharField(max_length=4,
                            help_text="Введите год издания",
                            verbose_name="Год издания")
    author = models.ManyToManyField('Author',
                                    help_text="Выберите автора (авторов)
                                    книги",
                                    verbose_name="Автор (авторы) книги")
    summary = models.TextField(max_length=1000,
                               help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13,
                            help_text="Должно содержать 13 символов",
                            verbose_name="ISBN книги")
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text="Введите цену книги",
                                verbose_name="Цена (руб.)")
    photo = models.ImageField(upload_to='images',
                              help_text="Введите изображение обложки",
                              verbose_name="Изображение обложки")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает URL-адрес для доступа к
        # определенному экземпляру книги
        return reverse('book-detail', args=[str(self.id)])
