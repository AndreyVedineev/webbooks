from django.contrib import admin

from catalog.models import Author, Book, BookInstance, Genre, Language, Publisher, Status

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Status)
admin.site.register(BookInstance)



