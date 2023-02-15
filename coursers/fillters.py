from django_filters import rest_framework
from .models import Courses


class CoursesFillter(rest_framework.FilterSet):
    class Meta:
        model = Courses
        fields = {
            'name' : ['icontains'],
            'price' : ['lte', 'gte'],
        }