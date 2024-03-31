from django.contrib import admin
from .models import *
admin.site.register([ CourseCategory, CourseProduct, Course,Topic, Note,
                      InProgressCourse,Lesson,CompletedCourse
                      ])
