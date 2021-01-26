from django.core import validators
from django import forms
from .models import User

class TeacherRegistration(forms.ModelForm):
	class Meta:
		model=User
		fields=['firstname','lastname','profilepic','email','phone','room','subjects']
		widgets={
			'firstname':forms.TextInput(attrs={'class':'form-control'}),
			'lastname':forms.TextInput(attrs={'class':'form-control'}),
			'profilepic':forms.FileInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'phone':forms.TextInput(attrs={'class':'form-control'}),
			'room':forms.TextInput(attrs={'class':'form-control'}),
			'subjects':forms.TextInput(attrs={'class':'form-control'}),
		}