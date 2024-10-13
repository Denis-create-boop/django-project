from .models import Fridge
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class FridgeForm(ModelForm):
    class Meta:
        model = Fridge
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка холодильника'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель холодильника'
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