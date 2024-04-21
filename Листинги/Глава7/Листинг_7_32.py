from django import forms


class UserForm(forms.Form):
    time = forms.DateField(label="Введите время")
