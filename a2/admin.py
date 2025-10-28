from django.contrib import admin

# Register your models here.
from .models import HRLogin 
from .models import Job 

admin.site.register(HRLogin)
admin.site.register(Job)