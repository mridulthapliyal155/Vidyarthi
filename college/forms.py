from django import forms


class Years_of_experience(forms.Form):
    Years_of_experience = forms.IntegerField()


class Email_send(forms.Form):
    college_email = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


COLLEGE_CHOICES = [
    (0,'Government'),
    (1,'Private'),
]

class collegeSuggestionForm(forms.Form):
    Rating      = forms.FloatField(help_text='Please rate from 1 to 5')
    collegeType = forms.CharField(label='College Type',widget=forms.Select(choices=COLLEGE_CHOICES))
    avgFees     = forms.CharField(label = 'Average Fees')
