from django import forms
from models import Whatever

class UploadFileForm(forms.Form):
	file = forms.FileField()