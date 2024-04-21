# добавлено для редактирования книг
from .models import Book


# форма для изменения сведений о книгах
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
