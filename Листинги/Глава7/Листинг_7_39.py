from django import forms


class UserForm(forms.Form):
    date_time = forms.SplitDateTimeField(label="Введите дату и время")
