# import form class from django
from django import forms

from .models import User


# create a ModelForm
class UserAddForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User
        fields = ['username', 'email']