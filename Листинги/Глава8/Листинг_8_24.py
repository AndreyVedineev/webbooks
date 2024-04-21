from .models import File  # для работы с файлами


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
