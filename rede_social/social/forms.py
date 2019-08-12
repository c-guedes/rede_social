from django import forms
from django.forms.widgets import ClearableFileInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class PublicForm(forms.ModelForm):
    pub_text = forms.CharField(widget = forms.Textarea(attrs={'cols': 100, 'rows': 10}),required=True,max_length=200)

    class Meta:
        model = Public
        fields = ('pub_text',)

class CommentForm(forms.ModelForm):
    coment = forms.CharField(widget=forms.Textarea,max_length=200)

    class Meta:
        model = CommentPub
        fields = ('coment',)

    

