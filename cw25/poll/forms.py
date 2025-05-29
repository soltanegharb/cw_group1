from django import forms
from poll.models import Choice

class PostForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
