from .models import Muse
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class MuseForm(ModelForm):
    class Meta:
        model = Muse
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка аккустики'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель аккустики'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата добавления'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'описание'
            })
        }