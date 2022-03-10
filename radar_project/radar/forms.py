from django.contrib.auth.models import User
from radar.models import UserProfile
from django import forms

# Please update basing on the requirements of our implementation


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age','picture')
