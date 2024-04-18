from django.contrib import admin

# Register your models here.
from appa.models import *
admin.site.register(Topic)

admin.site.register(WebPages)

admin.site.register(AccessRecord)
