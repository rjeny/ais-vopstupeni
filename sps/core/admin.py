from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.University)
admin.site.register(models.City)
admin.site.register(models.Notification)
admin.site.register(models.StudentsOrganisation)