from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите ФИО")
    age = forms.IntegerField(label="Возраст", help_text="Введите возраст")
