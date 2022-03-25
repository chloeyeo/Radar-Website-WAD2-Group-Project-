from django.contrib.auth.models import User
from radar.models import UserProfile, Post
from django import forms
from django.forms import ModelForm
# Please update basing on the requirements of our implementation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        labels = {
            'username': '',
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': '',

        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'passord'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Last name'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age', 'picture')

        labels = {
            'age': '',
            'picture': '',
        }

        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control', 'value': '18', 'id': 'id_age'}),
            'picture': forms.ClearableFileInput(attrs={'class': "form-control form-control-lg", 'id': "formFileLg", 'type': "file", }),
        }


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
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place description', 'id': "exampleFormControlTextarea1", 'rows': "3"}),
            'image': forms.ClearableFileInput(attrs={'class': "form-control form-control-lg", 'id': "formFileLg", 'type': "file", }),
        }


# update profile forms
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': '',
            'email': '',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        }


# class UpdateProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput(
#         attrs={'class': 'form-control-file'}))
#     bio = forms.CharField(widget=forms.Textarea(
#         attrs={'class': 'form-control', 'rows': 5}))

#     class Meta:
#         model = Profile
#         fields = ['avatar', 'bio']
