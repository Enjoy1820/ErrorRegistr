import django.contrib.auth.forms
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(django.contrib.auth.forms.UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


from django.db import models

# Create your models here.
