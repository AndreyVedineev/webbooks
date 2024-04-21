from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15,
                           help_text="ФИО не более 15 символов")
