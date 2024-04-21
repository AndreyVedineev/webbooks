from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(label="Электронный адрес")
    reklama = forms.BooleanField(label="Согласны получать рекламу")
