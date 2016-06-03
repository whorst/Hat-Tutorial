from django.conf.urls import include
from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^home$', views.home, name = 'home'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^thanks$', views.thanks, name = 'thanks'),

]
