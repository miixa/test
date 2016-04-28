from django.contrib import admin
# Register your models here.
from apptestov import models

admin.site.register(models.user)
admin.site.register(models.Subject)
admin.site.register(models.Theme)
admin.site.register(models.Lesson)
admin.site.register(models.Question)
admin.site.register(models.Answer)
