from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

CHOICES = [("landlord", "Give on Rent"), ("tenant", "Take on Rent")]


# Inherit the Default UserCreation form
class SignUpForm(UserCreationForm):
    mobile_no = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    password1 = forms.CharField(
        label=("Enter Pssword"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label=("Confirm Password"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        # Use the custom User Model that we changed.
        model = User
        fields = (
            "email",
            "mobile_no",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class PropertyRent(forms.ModelForm):
    lease_type = forms.ChoiceField(
        choices=[("f", "Family"), ("a", "Anyone"), ("c", "Company")],
        widget=forms.Select(
            attrs={"class": "js-example-basic-single js-states form-control"}
        ),
    )
    furnished = forms.ChoiceField(
        choices=[("0", "Not Furnished"), ("1", "Fully Furnished")],
        widget=forms.RadioSelect(),
    )
    rooms = forms.ChoiceField(
        choices=[("1", "1BHK"), ("2", "2BHK"), ("3", "3BHK"), ("4", "4BHK")],
        widget=forms.Select(
            attrs={"class": "js-example-basic-single js-states form-control"}
        ),
    )

    class Meta:
        model = Properties
        fields = (
            "property_name",
            "lease_type",
            "furnished",
            "address",
            "rooms",
        )
        widgets = {
            "property_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
        }


class SearchForm(forms.Form):
    lease_type = forms.ChoiceField(
        choices=[("f", "Family"), ("a", "Anyone"), ("c", "Company")],
        widget=forms.Select(
            attrs={"class": "js-example-basic-single js-states form-control"}
        ),
    )
    furnished = forms.ChoiceField(
        choices=[("0", "Not Furnished"), ("1", "Fully Furnished")],
        widget=forms.RadioSelect(),
    )
    rooms = forms.ChoiceField(
        choices=[("1", "1BHK"), ("2", "2BHK"), ("3", "3BHK"), ("4", "4BHK")],
        widget=forms.Select(
            attrs={"class": "js-example-basic-single js-states form-control"}
        ),
    )
