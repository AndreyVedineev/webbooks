from django import forms


class UserForm(forms.Form):
    num = forms.IntegerField(label="Введите целое число")
