from django.contrib.auth.models import User
from radar.models import UserProfile, Post
from django import forms
from django.forms import ModelForm
# Please update basing on the requirements of our implementation


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age', 'picture')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('category', 'title', 'description', 'image')

# bootstrap formatting
        labels = {
            'title': '',
            'description': '',
        }

        widgets = {
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'category'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place description', }),
            'image': forms.ClearableFileInput(attrs={'class': "form-control form-control-lg", 'id': "formFileLg", 'type': "file", }),
        }
