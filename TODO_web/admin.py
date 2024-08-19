from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.consumers)
admin.site.register(models.Todo)