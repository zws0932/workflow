from django.contrib import admin

# Register your models here.
from workflow.models import *

admin.site.register(Workorder)
admin.site.register(Task)
