from django import forms


class UserForm(forms.Form):
    time_delta = forms.DurationField(label="Введите промежуток времени")
