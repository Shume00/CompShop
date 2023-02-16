from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Users


# Create your forms here.

class NewUserForm(UserCreationForm):
    nameofuser = forms.TextInput(attrs={'required': True})

    class Meta:
        model = Users
        fields = ("username", "nameofuser", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.nameofuser = self.cleaned_data['nameofuser']
        if commit:
            user.save()
        return user