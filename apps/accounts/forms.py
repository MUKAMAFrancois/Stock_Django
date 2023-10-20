from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.accounts.models import Profile

class CreatingUserForm(UserCreationForm):
    #inherit
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['email','username','password1','password2']


class Updating_User_Profile_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['adress','phone','image']

class Updating_User_Credintials(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']