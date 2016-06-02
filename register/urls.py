from django.conf.urls import include
from django.conf.urls import url
from . import views

app_name = 'register'

urlpatterns = [

    url(r'^register/(?P<pk>\d+)/$', views.Register.as_view(), name = 'register')

]
