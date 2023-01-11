from django import forms
from main.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'contact')
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                }
            ),
            'contact': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telegram, @mikemka',
                    'data-length': 128,
                }
            ),
        }
