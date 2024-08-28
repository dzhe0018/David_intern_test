from django import forms
from .models import Entry

#define a form for name and age
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'age']
