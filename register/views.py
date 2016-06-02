from django.shortcuts import render
from django.views import generic
# Create your views here.

class Register(generic.DetailView):
    template_name = 'register/reg.html'

    def get_queryset(self):
        print("Hello!")
