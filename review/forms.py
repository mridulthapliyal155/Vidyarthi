from django import forms
from .models import Review,Seconday_model

class Review_Form(forms.ModelForm):
    class Meta:
        model   = Review
        fields  = [
            'rating',
            'know_us',
            'recommend',
            'suggestion',
        ]

class Seconday_form(forms.ModelForm):
    class Meta:
        model  = Seconday_model
        fields = [
            'interest',
            'college',
            'interest_college',
            'if_college',
            'reason',
        ] 
