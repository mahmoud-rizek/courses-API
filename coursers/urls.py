from django.urls import path
from .views import  CoursesApi, CoursesApiDetail
app_name = 'coursers'



urlpatterns = [
    # path("api/", course_api),
    path("api/", CoursesApi.as_view()),
    path("api/<int:pk>", CoursesApiDetail.as_view())
]
