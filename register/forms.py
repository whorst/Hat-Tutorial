from django import forms
from django.db import models
from django.forms import ModelForm
from django import forms
from models import ShirtOptions, FrisbeeOptions, Person
import re
from django.core.exceptions import ValidationError

#PersonForm is simply a ModelForm for the Person class

def valid_phone_number(phone_var):
    pattern = re.compile('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
    j = pattern.match(phone_var)

    if j:
        return True
    else:
        return False

class PersonForm(ModelForm):

    #These next two lines will appear as multiple checkboxes
    shirt_options = forms.ModelMultipleChoiceField(queryset=ShirtOptions.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    frisbee_options = forms.ModelMultipleChoiceField(queryset=FrisbeeOptions.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)


    # def clean(self):
    #     self.

    #


    def clean_phone_number(self):
        #print (self.cleaned_data)
        phone_number = self.cleaned_data['phone_number']
        if(valid_phone_number(phone_number) == False):
           raise ValidationError('Incorrect Phone Number')
        return phone_number




    class Meta:
        model = Person
        fields = '__all__'
