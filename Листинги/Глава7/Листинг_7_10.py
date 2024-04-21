from django import forms


class UserForm(forms.Form):
    basket = forms.BooleanField(label="Положить товар в корзину", required=False)
