from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Registration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

from django.forms import ValidationError

def clean_email(self):
    email = self.cleaned_data['email']

    if not email.endswith('@cowhite.com'):
        raise ValidationError('Domain of email is not valid')

    return email