from django import forms 

class uploadFormFiles(forms.Form):
    file = forms.FileField()