from django.contrib import admin
from service.models import Course_Details

class Course_Admin(admin.ModelAdmin):

    list_display = ['c_name', 'c_duration', 'c_faculty_name']

admin.site.register(Course_Details,Course_Admin)
