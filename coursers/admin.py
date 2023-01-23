from django.contrib import admin
from .models import Courses, CourseReviews, Instructor, Content
# Register your models here.
class Instructoradmin(admin.ModelAdmin):
    list_display = ['name','id']
    
admin.site.register(CourseReviews)
admin.site.register(Courses)
admin.site.register(Instructor,Instructoradmin )
admin.site.register(Content)
