from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import generics

from .models import Content, CourseReviews, Courses, Instructor, CourseReviews
from .serializer import CourseSerializer, InstractorSerializer, ContentSerializer
from .paginations import CoursePaginations
from .fillters import CoursesFillter

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
    pagination_class = CoursePaginations
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    filterset_class = CoursesFillter
    # search_fields = ['name']
    # permission_classes = [IsAuthenticated]