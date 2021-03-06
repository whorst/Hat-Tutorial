from __future__ import unicode_literals
from django import forms
from django.db import models
from django.forms import ModelForm
import re
from django import forms
from localflavor.us.models import PhoneNumberField

SHIRT = 'Shirt'
FRISBEE = 'Frisbee'

SMALL = 'S'
MEDIUM = 'M'
LARGE = 'L'

MALE = 'M'
FEMALE = 'F'
PREF = 'Pref'

IN_CUTTER = 'In Cutter'
OUT_CUTTER = 'Out Cutter'
SHORT_DISTANCE_HANDLER = 'Short Distance Handler'
LONG_DISTANCE_HANDLER = 'Long Distanc Handler'
#Every single dropdown CharField requires tuples.

SKILL_CHOICES = (
    ('1','1   Amateur'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5   Pro'),
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

POSITION_CHOICE = (
    (IN_CUTTER, 'In Cutter'),
    (OUT_CUTTER, 'Out Cutter'),
    (SHORT_DISTANCE_HANDLER, 'Short Distance Handler'),
    (LONG_DISTANCE_HANDLER, 'Long Distance Handler'),
)


class ShirtOptions(models.Model):
    """
    ShirtOptions helps our ModelForm to render a multi-checkbox form.
    """

    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description


class FrisbeeOptions(models.Model):
    """
    FrisbeeOptions helps our ModelForm to render a multi-checkbox form.
    """

    description = models.CharField(max_length=300)
    def __str__(self):
        return self.description



class Person(models.Model):
    """
    Person contains the information that our user fills out in anticipation of the event
    """

    #The next four lines are regular text boxes
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 13)

    #These two lines are for the two checkboxes
    shirt_options = models.ManyToManyField(ShirtOptions)
    frisbee_options = models.ManyToManyField(FrisbeeOptions)

    #The following charfields will appear as dropdown boxes
    sex = models.CharField(max_length = 100, choices=SEX_CHOICE,)
    skill = models.CharField(max_length = 200, choices= SKILL_CHOICES, default = '1',)
    shirt_size = models.CharField(max_length = 200,choices = SHIRT_CHOICE,default = 'Small',)
    position = models.CharField(max_length = 200,choices = POSITION_CHOICE,default = 'In Cutter',)

    def __str__(self):
        return('{first} {last}'.format(first=self.first_name, last=self.last_name))
