from .models import Utug
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class UtugForm(ModelForm):
    class Meta:
        model = Utug
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка утюга'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель утюга'
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