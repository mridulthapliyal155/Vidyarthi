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

STATE_CHOICES = [   
    (	23	,	'Odisha'),
(	18	,	'Maharashtra'),
(	8	,	'Delhi'	),
(	14	,	'Jharkhand'	),
(	29	,	'Telangana'	),
(	15	,	'Karnataka'	),
(	31	,	'Uttar Pradesh'	),
(	25	,	'Punjab'),
(	28	,	'Tamil Nadu'	),
(	10	,	'Gujarat'	),
(	33	,	'West Bengal'	),
(	16	,	'Kerala'	),
(	11	,	'Haryana'	),
(	26	,	'Rajasthan'	),
(	17	,	'Madhya Pradesh'	),
(	3	,	'Assam'	),
(	5	,	'Chandigarh'	),
(	1	,	'Andhra Pradesh'	),
(	6	,	'Chhattisgarh'	),
(	4	,	'Bihar'	),
(	12	,	'Himachal Pradesh'	),
(	19	,	'Manipur'	),
(	32	,	'Uttarakhand'	),
(	30	,	'Tripura'	),
(	9	,	'Goa'	),
(	13	,	'Jammu and Kashmir'	),
(	24	,	'Puducherry'	),
(	20	,	'Meghalaya'	),
(	2	,	'Arunachal Pradesh'	),
(	22	,	'Nagaland'	),
(	21	,	'Mizoram'	),
(	27	,	'Sikkim'	),
(	0	,	'Andaman and Nicobar Islands'	),
(	7	,	'Dadra and Nagar Haveli'	),
]

class collegeSuggestionForm(forms.Form):
    Rating      = forms.FloatField(help_text='Please rate from 1 to 5')
    collegeType = forms.CharField(label='College Type',widget=forms.Select(choices=COLLEGE_CHOICES))
    State = forms.CharField(widget=forms.Select(choices=STATE_CHOICES))
    avgFees     = forms.CharField(label = 'Average Fees')
