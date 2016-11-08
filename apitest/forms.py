from django import forms

class NameForm(forms.Form):
	apikey = forms.CharField(label='APIKEY', max_length=1000)
	secretkey = forms.CharField(label='Secret   ', max_length=1000, widget=forms.Textarea)
