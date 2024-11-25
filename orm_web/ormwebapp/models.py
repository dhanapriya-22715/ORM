from django.db import models
from django.contrib import admin
class Employee (models.Model):
    Eid=models.CharField(max_length=20,help_text="Employee ID")
    Name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('Eid','Name','salary','age','email')

