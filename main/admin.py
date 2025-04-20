from django.contrib import admin

# Register your models here.

from .models import Project, Certificate

admin.site.register(Project)
admin.site.register(Certificate)