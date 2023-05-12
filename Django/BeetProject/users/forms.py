from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'your_nick_name'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'super_secret_password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
