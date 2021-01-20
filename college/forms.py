from django import forms


class Years_of_experience(forms.Form):
    Years_of_experience = forms.IntegerField()


class Email_send(forms.Form):
    college_email = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
