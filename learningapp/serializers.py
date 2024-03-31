from rest_framework import serializers
from .models import *
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
class UserRegistrationSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    class Meta:
        model = User        
        fields =fields = '__all__'        

    def create(self, validated_data):
        user_data = { 
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            
            'username': validated_data['email'],         
            'email': validated_data['email'],
            'password': validated_data['password'],
        }
              
        return User.objects.create_user(**user_data)
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id', 'username', 'email', 'first_name', 'last_name']
class CourseCategorySerializer (serializers.ModelSerializer):    
    class Meta:
        model = CourseCategory 
        fields = '__all__'

class CourseProductSerializer (serializers.ModelSerializer):    
    class Meta:
        model = CourseProduct 
        fields = '__all__'

class CourseSerializer (serializers.ModelSerializer):    
    class Meta:
        model = Course 
        fields = '__all__'

class NoteSerializer (serializers.ModelSerializer):    
    class Meta:
        model = Note 
        fields = '__all__'

class GetNoteSerializer (serializers.ModelSerializer):
    topic = serializers.ReadOnlyField(source='topic.name')    
    class Meta:
        model = Note 
        fields = ['id','topic','subtopic', 'content','name']


class LessonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CollectionCourseSerializer (serializers.ModelSerializer):
    class Meta:
        model = InProgressCourse
        fields = '__all__' 
class CompletedCourseSerializer (serializers.ModelSerializer):
    class Meta:
        model = CompletedCourse
        fields = '__all__'