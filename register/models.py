from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here

#CHOICES is simply the user's choice for the sex_field
CHOICES = (('1','Male'),('2','Female'))

#first_name is a text field that allows our user to enter their first name
class first_name(models.Model):

    first_name_field = models.charField(max_length = 200)

#last_name is a text field that allows our user to enter their last name
class last_name(models.Model):

    last_name_field = models.charField(max_length = 200)

#email is a field that allows our user to enter their email account
class email(models.Model):

    email_field = models.charField(max_length = 300)

#phone_number is a field that allows the user to enter their phone number
class phone_number(models.Model):

    phone_number_field = models.charField(max_length = 50)

#first_name is a radio widget that allows our user to pick their gender
class sex(models.Model):

    sex_field = forms.ChoiceField(widget=forms.RadioSelect, choies = CHOICES)

'''
class skill(models.Model):


class buy_options(models.Model):


class shirt_size(models.Model):


class position(models.Model):
'''
