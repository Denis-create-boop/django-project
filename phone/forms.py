from .models import Phone
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['title', 'model', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'марка телефона'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'модель телефона'
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