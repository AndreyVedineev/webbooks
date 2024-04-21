from django import forms


class UserForm(forms.Form):
    country = forms.MultipleChoiceField(label="Выберите страны",
                                        choices=((1, "Англия"),
                                                 (2, "Германия"),
                                                 (3, "Испания"),
                                                 (4, "Россия")))
