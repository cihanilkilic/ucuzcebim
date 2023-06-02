from django import forms
from.models import *

class ContactModelForms(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'