from django.contrib import admin
from .models import Student  # Make sure the model name matches

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email']
