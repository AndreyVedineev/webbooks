# издательство
class Publisher(models.Model):
    name = models.CharField(max_length=20,
                            help_text=" Введите наименование издательства",
                            verbose_name="Издательство")

    def __str__(self):
        return self.name
