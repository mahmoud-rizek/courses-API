from django.shortcuts import render
from .models import Content, CourseReviews, Courses, Instructor, CourseReviews
from .serializer import CourseSerializer, InstractorSerializer, ContentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import generics

# @api_view('GET')
# def course_api(request):
#     queryset = Courses.objects.all()
#     data = CourseSerializer(queryset).data
#     return Response({'allProduct':data})


class CoursesApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses
    serializer_class = CourseSerializer






class CoursesApi(generics.ListCreateAPIView):
    queryset = Courses
    serializer_class = CourseSerializer
    # pagination_class = paginationStyleName
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'price']
    # filterset_class = fillterName
    # search_fields = ['name']
    # permission_classes = [IsAuthenticated]