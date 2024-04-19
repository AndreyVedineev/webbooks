from unittest import mock
from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Введите жанр книги", verbose_name="Жанар книги"
    )

    def __str__(self) -> str:
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=20, help_text="Введите язык книги", verbose_name="Язык книги"
    )

    def __str__(self) -> str:
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Введите нименование издательсва",
        verbose_name="Издательство",
    )

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField(
        max_length=100, help_text="Введите имя автора", verbose_name="Имя автора"
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию автора",
        verbose_name="Фамилия автора",
    )
    date_of_birth = models.DateField(
        help_text="Введите дату рождения",
        verbose_name="Дата рождения",
        null=True,
        blank=True,
    )
    about = models.ImageField(
        upload_to="images",
        help_text="Введите фото автора",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.last_name


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Введите название книги",
        verbose_name="Название книги",
    )
    genre = models.ForeignKey(
        "Genre",
        on_delete=models.CASCADE,
        help_text="Выберите жанр книги",
        verbose_name="Жанр книги",
        null=True,
    )
    language = models.ForeignKey(
        "Language",
        on_delete=models.CASCADE,
        help_text="Выбереье язык книги",
        verbose_name="Язык книги",
        null=True,
    )
    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.CASCADE,
        help_text="Выберите издательство",
        verbose_name="Издательство",
        null=True,
    )
    year = models.CharField(
        max_length=4,
        help_text="Введите год изздания",
        verbose_name="Год издания",
    )
    author = models.ManyToManyField(
        "Author",
        help_text="Выберете автора (авторов) книги",
        verbose_name="Автор (авторы) книги",
    )
    summary = models.TextField(
        max_length=1000,
        help_text="Введите краткое описание книги",
        verbose_name="Анотация книги",
    )
    isbn = models.CharField(
        max_length=13,
        help_text="Должен содержать 13 символов",
        verbose_name="ISBN книги",
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        help_text="Введите цену книги",
        verbose_name="Цена (руб.)",
    )
    photo = models.ImageField(
        upload_to="images",
        help_text="Введите изображение обложки",
        verbose_name="Изображение обложки",
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

    class Status(models.Model):
        name = models.CharField(
            max_length=20,
            help_text="Введите статус книги",
            verbose_name="Статус экземпляра книги",
        )

        def __str__(self) -> str:
            return self.name

    class BookInstance(models.Model):
        book = models.ForeignKey("Book", on_delete=models.CASCADE, null="True")
        inv_nom = models.CharField(
            max_length=20,
            null=True,
            help_text="Введите инвентарный номер",
            verbose_name="Инвентарный номер",
        )
        status = models.ForeignKey(
            "Status",
            on_delete=models.CASCADE,
            null=True,
            help_text="Изменить состояние экземпляра",
        )
        due_back = models.DateField(
            null=True,
            blank=True,
            help_text="Введите конец срока статуса",
            verbose_name="Дата окончания статуса",
        )

        class Meta:
            ordering = [
                "due_back",
            ]

        def __str__(self) -> str:
            return f"{self.inv_nom} -  {self.book} - {self.status}"
