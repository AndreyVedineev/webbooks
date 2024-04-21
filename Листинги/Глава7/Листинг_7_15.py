from django import forms


class UserForm(forms.Form):
    date_time = forms.DateTimeField(label="Введите дату и время")
