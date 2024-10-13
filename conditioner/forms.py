from .models import Condition
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ConditionForm(ModelForm):
    class Meta:
        model = Condition
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка кондиционера'
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