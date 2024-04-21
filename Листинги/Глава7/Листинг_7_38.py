from django import forms


class UserForm(forms.Form):
    combo_text = forms.MultiValueField(label='Комплексное поле',
                                       fields=(
                                           forms.CharField(max_length=20),
                                           forms.EmailField()))
