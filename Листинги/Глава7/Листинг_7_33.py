from django import forms


class UserForm(forms.Form):
    city = forms.TypedChoiceField(label="Выберите город",
                                  empty_value=None,
                                  choices=((1, "Москва"),
                                           (2, "Воронеж"),
                                           (3, "Курск")))
