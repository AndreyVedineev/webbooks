from django import forms


class UserForm(forms.Form):
    uuid_text = forms.UUIDField(label="Введите UUID",
                                help_text="Формат xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
