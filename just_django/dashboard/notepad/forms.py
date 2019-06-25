from django import forms
from notepad.models import *

class NoteModelForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['title','url','image']