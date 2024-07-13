from django.contrib import admin
from .models import User, Task
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(User)
@admin.register(Task)
class userdata(ImportExportModelAdmin):
    pass