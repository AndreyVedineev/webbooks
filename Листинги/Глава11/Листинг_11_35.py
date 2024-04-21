# добавлено для редактирования авторов
from .models import Author


# форма для изменения сведений об авторах
class Form_edit_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
