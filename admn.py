# In jobs/admin.py
from django.contrib import admin
from .models import Job

admin.site.register(Job)

# In accounts/admin.py
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)