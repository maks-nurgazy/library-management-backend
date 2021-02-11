from django import forms
from django.core.exceptions import ObjectDoesNotExist

from users.models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': "Enter Email Address...",
               'id': "exampleInputEmail", 'aria-describedby': "emailHelp"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': "Password",
               'id': "exampleInputPassword"}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
            valid = user.check_password(password)
            if not valid:
                raise forms.ValidationError("Check your username/password")
        except ObjectDoesNotExist:
            raise forms.ValidationError("Check your username/password")
