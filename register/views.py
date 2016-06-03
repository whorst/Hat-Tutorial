from django.shortcuts import render
from django.views import generic

# Create your views here.
'''
class Register(generic.DetailView):  #look at different views
    template_name = 'register/reg.html'

    def get_queryset(self):
        print("Hello!")
'''

def home(request):
    return render(request, "register/home.html",{})


def register(request):
    return render(request, "register/reg.html",{})

def thanks(request):
    return render(request, "register/thanks.html",{})
