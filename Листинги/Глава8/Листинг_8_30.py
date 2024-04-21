from .models import VideoFile  # для работы с файлами видео


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = '__all__'
