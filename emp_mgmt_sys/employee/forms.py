from django import forms
from django.contrib.auth.models import User, Group
from django.db import models
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	role = forms.ModelChoiceField(queryset = Group.objects.all())

	class Meta:
		model = User
		fields = ['first_name', 'last_name','email','username','password']

		#excludes = ['']

		label = {
		  'password' : "password"
		}	

	# def clean_email(self):
	# 	if self.cleaned_data['email'].endsWith("@gmail.com"):
	# 		return self.cleaned_data['email']
	# 	else:
	# 		return ValidationError("this is not a valid email")
	def save(self):
		password = self.cleaned_data.pop('password')
		role = self.cleaned_data.pop('role')
		u = super().save()
		u.groups.set([role])
		u.set_password(password)
		u.save()
		return u

	def __init__(self, *args, **kwargs):
		if kwargs.get("instance"):
			initial = kwargs.setdefault('initial',{})
			if kwargs['instance'].groups.all():
				initial['role'] =  kwargs['instance'].groups.all()[0]
			else:
				initial['role'] = None	
		forms.ModelForm.__init__(self, *args, **kwargs)