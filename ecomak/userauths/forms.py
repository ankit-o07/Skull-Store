from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": 'Username'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={"placeholder": 'Email'}))
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={"placeholder": 'Password'}))
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={"placeholder": 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email']

