from django import forms
from notes.models import Note


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body', 'author')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Note Text'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_id', 'type': 'hidden'}),

        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Note Text'}),

        }
