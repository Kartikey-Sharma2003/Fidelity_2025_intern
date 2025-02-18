from django.contrib import admin
from .models import Manager

class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname','salary','doj','manages']


admin.site.register(Manager,ManagerAdmin)


# Register your models here.
