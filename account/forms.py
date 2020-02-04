from django import forms
from django.contrib.auth.models import User
from .models import OTPUser
from django.contrib.auth.forms import UserCreationForm

class OTPForm(forms.Form):
    """
    OTP form to authenticate the user
    """

    username = forms.CharField()

    otp = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'OTP'}),
    )


    def clean(self):
        if not self.cleaned_data.get('otp'):
            raise forms.ValidationError({
                'otp': 'Invalid OTP'
            })

        return self.cleaned_data

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    gender = forms.CharField(max_length=1, help_text='gender')
    phone_number = forms.IntegerField(help_text='Phone Number')
 
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','gender','phone_number', 'password1', 'password2',)