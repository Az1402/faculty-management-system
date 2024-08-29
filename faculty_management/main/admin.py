from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Dean, Department, Announcement, Message, Complaint

admin.site.register(Dean)
admin.site.register(Department)
admin.site.register(Announcement)
admin.site.register(Message)
admin.site.register(Complaint)

