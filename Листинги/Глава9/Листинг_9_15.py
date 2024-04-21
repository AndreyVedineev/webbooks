# экземпляр книги
class BookInstance(models.Model):
    book = models.ForeignKey('Book',
                             on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(
        max_length=20,
        null=True,
        help_text="Введите инвентарный номер экземпляра",
        verbose_name="Инвентарный номер")
    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE,
                               null=True,
                               help_text='Изменить состояние экземпляра',
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True,
                                blank=True,
                                help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")

    # Метаданные
    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
