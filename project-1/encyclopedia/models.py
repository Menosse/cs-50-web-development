from django.db import models
from django import forms
# Create your models here.

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Entry Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Entry content", widget=forms.Textarea(attrs={'class': 'form-control'}))

class EditForm(forms.Form):
    content = forms.CharField(label="Edit content", widget=forms.Textarea(attrs={'class': 'form-control'}))