from django import forms
# from django.db import transaction
# from django.contrib.auth.forms import UserCreationForm
# from django.forms.utils import ValidationError
from .models import *


class CreateStream(forms.ModelForm):
    class Meta:
        model = Stream
        fields = [ 'name']


class CreateStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'first_name', 'last_name', 'age', 'stream']


class EditStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'first_name', 'last_name', 'age', 'stream']