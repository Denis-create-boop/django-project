from .models import Tv
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TvForm(ModelForm):
    class Meta:
        model = Tv
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка телевизора'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель телевизора'
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