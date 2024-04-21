from django import forms


class UserForm(forms.Form):
    slug_text = forms.SlugField(label="Введите текст")
