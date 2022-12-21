from django.contrib import admin
from .models import Student, Admin, Room

# Register your models here.
admin.site.register([Student, Admin, Room])
