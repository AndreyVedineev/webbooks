from django import forms


class UserForm(forms.Form):
    file = forms.ImageField(label="Изображение")
