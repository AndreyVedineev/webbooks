from django import forms


class UserForm(forms.Form):
    file_path = forms.FilePathField(label="Выберите файл",
                                    path="C:/my_doc/",
                                    allow_files="True",
                                    allow_folders="True")
