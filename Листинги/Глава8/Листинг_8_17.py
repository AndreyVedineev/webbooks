from .models import Image  # для работы с изображениями


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        # fields = ['title', 'image']
