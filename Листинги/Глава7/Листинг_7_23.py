from django import forms


class UserForm(forms.Form):
    num = forms.FloatField(label="Введите число")
