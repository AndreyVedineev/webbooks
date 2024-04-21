from django import forms


class UserForm(forms.Form):
    date = forms.DateField(label="Введите дату")
