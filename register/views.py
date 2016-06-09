from django.shortcuts import render
from django.views import generic
import models
from models import PersonForm, Person
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

#This is our home url
def home(request):
    return render(request, "register/home.html", {})

#This is the url we use for registration
def register(request):
    personform = PersonForm()
    if request.method=='POST':
        personform = PersonForm(request.POST)
        if personform.is_valid():
            profile = personform.save(commit=False)
            profile.save()
            personform.save_m2m()
            return HttpResponseRedirect(reverse('thanks'))
        else:
            personform = PersonForm()
    return render(request, "register/reg.html", {'PersonForm': personform})

#This is the url thank you screen
def thanks(request):
    return render(request, "register/thanks.html",{})
