from __future__ import unicode_literals
from django import forms
from django.db import models
from django.forms import ModelForm
import re
from django import forms
import localflavor.us.models

SHIRT = "Shirt"
FRISBEE = "Frisbee"

SMALL = 'S'
MEDIUM = 'M'
LARGE = 'L'

MALE = 'M'
FEMALE = "F"
PREF = "Pref"

#Every single dropdown CharField requires tuples.

CHOICES = (
    ('1','Male'),
    ('2','Female'),
)

BUY_OPTIONS_LIST = (
    (SHIRT, 'shirt'),
    (FRISBEE,'frisbee'),
)

SHIRT_CHOICE = (
    (SMALL, 'S'),
    (MEDIUM,'M'),
    (LARGE,'L'),
)

SEX_CHOICE = (
    (MALE, 'Male'),
    (FEMALE,'Female'),
    (PREF,'Prefer Not to Respond'),
)

class ShirtOptions(models.Model):
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description

class FrisbeeOptions(models.Model):
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.description


#Person contains the information that our user fills out in anticipation of the event
class Person(models.Model):

    #The next four lines are regular text boxes
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone_number = localflavor.us.models.PhoneNumberField()

    #These two lines are for the two checkboxes
    shirt_options = models.ManyToManyField(ShirtOptions)
    frisbee_options = models.ManyToManyField(FrisbeeOptions)

    #The following charfields will appear as dropdown boxes
    sex = models.CharField(max_length = 100, choices=SEX_CHOICE,)
    skill = models.CharField(max_length = 200, choices=((str(x), x) for x in range(1, 6)), default = 1,)
    shirt_size = models.CharField(max_length = 200,choices = SHIRT_CHOICE,default = 'Small',)




#PersonForm is simply a ModelForm for the Person class
class PersonForm(ModelForm):

    #These next two lines will appear as multiple checkboxes
    shirt_options = forms.ModelMultipleChoiceField(queryset=ShirtOptions.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    frisbee_options = forms.ModelMultipleChoiceField(queryset=FrisbeeOptions.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Person
        fields = '__all__'
