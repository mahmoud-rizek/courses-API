from .models import Courses, Instructor, Content
from rest_framework import serializers
# Create your APIs here.
class InstractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # content = ContentSerializer()
    teacher = InstractorSerializer()
    class Meta:
        model = Courses
        fields = '__all__'


 
