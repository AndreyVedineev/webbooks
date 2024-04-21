from django import forms


class UserForm(forms.Form):
    combo_text = forms.ComboField(label='Введите данные',
                                  fields=[
                                      forms.CharField(max_length=20),
                                      forms.EmailField()])
