from django.contrib import admin
from .models import Courses, CourseReviews, Instructor, Content
# Register your models here.

admin.site.register(CourseReviews)
admin.site.register(Courses)
admin.site.register(Instructor)
admin.site.register(Content)
