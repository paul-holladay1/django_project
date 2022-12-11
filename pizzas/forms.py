from django import forms

from .models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}