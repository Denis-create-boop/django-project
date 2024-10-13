from .models import Computer
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка компьютера'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата добавления'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'описание'
            })
        }
