from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Returns a form regsiter form
    """
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name'
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})


class UserUpdateForm(forms.ModelForm):
    """
    Returns a form update profile form
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})


class ProfileRegisterForm(forms.ModelForm):
    """
    Returns a form regsiter form
    """
    class Meta:
        model = Profile
        fields = [
            'gender',
            'address1',
            'address2',
            'city',
            'postcode',
            'mobile',
            'dob',
            'height'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileRegisterForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class' : 'form-select'})
        self.fields['address1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['address2'].widget.attrs.update({'class' : 'form-control'})
        self.fields['city'].widget.attrs.update({'class' : 'form-control'})
        self.fields['postcode'].widget.attrs.update({'class' : 'form-control'})
        self.fields['mobile'].widget.attrs.update({'class' : 'form-control'})
        self.fields['dob'].widget.attrs.update({'class' : 'form-control'})
        self.fields['height'].widget.attrs.update({'class' : 'form-control'})
