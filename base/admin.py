from django.contrib import admin

# Register your models here.
from .models import Project, Topic, About

admin.site.register(Project)
admin.site.register(Topic)
admin.site.register(About)