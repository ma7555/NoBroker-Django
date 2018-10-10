from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

CHOICES=[('landlord','Give on Rent'),('tenant','Take on Rent')]

#Inherit the Default UserCreation form
class SignUpForm(UserCreationForm):
	mobile_no = forms.CharField(max_length=10, required=True)
	user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

	class Meta:
		#Use the custom User Model that we changed.
		model = User
		fields = ('email','mobile_no','first_name','last_name','password1','password2')

class PropertyRent(forms.ModelForm):
	lease_type = forms.ChoiceField(choices=[('f','Family'),('a','Anyone'),('c','Company')])
	furnished = forms.ChoiceField(choices=[('0','Not Furnished'),('1','Fully Furnished')], widget=forms.RadioSelect())
	rooms = forms.ChoiceField(choices=[('1','1BHK'),('2','2BHK'),('3','3BHK'),('4','4BHK')])
	class Meta:
		model = Properties
		fields = ('property_name','lease_type','furnished','address','rooms',)

class SearchForm(forms.Form):
	lease_type = forms.ChoiceField(choices=[('f','Family'),('a','Anyone'),('c','Company')])
	furnished = forms.ChoiceField(choices=[('0','Not Furnished'),('1','Fully Furnished')], widget=forms.RadioSelect())
	rooms = forms.ChoiceField(choices=[('1','1BHK'),('2','2BHK'),('3','3BHK'),('4','4BHK')])