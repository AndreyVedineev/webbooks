from django.contrib import admin

from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance


# Определяем класс AuthorAdmin для авторов книг
class AuthorAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Author)
# Регистрируем класс AuthorAdmin для авторов книг
admin.site.register(Author, AuthorAdmin)


# admin.site.register(Book)
# Регистрируем класс BookAdmin  для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


# admin.site.register(BookInstance)
# Регистрируем класс BookInstanceAdmin для экземпляров книг
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
