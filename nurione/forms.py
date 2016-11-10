from django import forms
from .models import TcEntries

class PostForm(forms.ModelForm):
    class Meta:
        model = TcEntries
        fields = ('title', 'content',)
