from django import forms

from users.models import User


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirm_password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'enter your email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your last name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter your password'}),
            'confirm_password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'confirm your password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match!')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


