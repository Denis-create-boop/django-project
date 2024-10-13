from .models import Wash
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class WashForm(ModelForm):
    class Meta:
        model = Wash
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка стиральной машины'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель стиральной машины'
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