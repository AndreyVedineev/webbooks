from django import forms
from datetime import date

from .models import Author


class Form_add_author(forms.Form):
    first_name = forms.CharField(label="Фамилия автора")
    last_name = forms.CharField(label="Имя автора")
    date_of_birth = forms.DateField(
        label="Дата рождения",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
    )
    about= forms.CharField(label='Сведения об авторе',
                           widget=forms.Textarea)
    photo = forms.ImageField(label='Фототавтора')

# форма для изменения сведений об авторах
class Form_edit_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'