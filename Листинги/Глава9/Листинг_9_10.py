# язык книги
class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text=" Введите язык книги",
                            verbose_name="Язык книги")

    def __str__(self):
        return self.name
