from django import forms

class CreateNewPoll(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    