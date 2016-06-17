from django.contrib import admin

from models import Person, ShirtOptions, FrisbeeOptions

# This will register your person Model and create a corresponding template on the admin page
admin.site.register(Person)
admin.site.register(ShirtOptions)
admin.site.register(FrisbeeOptions)
