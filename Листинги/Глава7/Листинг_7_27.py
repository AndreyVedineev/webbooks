from django import forms


class UserForm(forms.Form):
    num = forms.JSONField(label="Данные формата JSON")
