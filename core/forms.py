from django import forms

from .models import Campus

class PostForm(forms.ModelForm):

    class Meta:
        model = Campus
        fields = ('nombre', 'imagen',)