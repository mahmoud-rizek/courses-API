from django.contrib import admin
from .models import Courses, CourseReviews, Instructor, Content
# Register your models here.
class Instructoradmin(admin.ModelAdmin):
    list_display = ['name','id']
class Courseadmin(admin.ModelAdmin):
    list_display = ['name','id']
    
class Reviewsadmin(admin.ModelAdmin):
    list_display = ['id', 'user','course']
    
admin.site.register(CourseReviews, Reviewsadmin)
admin.site.register(Courses, Courseadmin)
admin.site.register(Instructor,Instructoradmin )
admin.site.register(Content)
