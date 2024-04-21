class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# admin.site.register(Book)
# Регистрируем класс BookAdmin  для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]
