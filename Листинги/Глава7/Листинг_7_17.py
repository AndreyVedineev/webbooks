from django import forms


class UserForm(forms.Form):
    num = forms.DecimalField(label="Введите десятичное число",
                             decimal_places=2)
