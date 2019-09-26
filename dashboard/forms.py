from django import forms
from .models import Leave
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave
        fields = ('name', 'department', 'reason', 'from_date', 'to_date',
                  'leave_type', 'phone_number', 'Person_in_charge', 'leave_days')
        widgets = {'leave_days': forms.HiddenInput()}


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email', 'password')
