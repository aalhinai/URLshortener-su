#forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder= "Username")), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder = "Email address")))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder = "Password")))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False, placeholder = "Password (again)")))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        print User.objects.filter(email=email).count()
        if email and User.objects.filter(email=email).count() > 0:
           raise forms.ValidationError(_("The email already exists. Please try another one."))
        return email



    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 != password2:
               raise forms.ValidationError(_("The two password fields did not match."))
        return password2



    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
           if self.cleaned_data['password1'] != self.cleaned_data['password2']:
              raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
