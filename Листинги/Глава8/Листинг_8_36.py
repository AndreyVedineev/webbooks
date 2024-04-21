from .models import AudioFile  # для работы с файлами аудио


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'
