from django.db import models

from django.contrib.auth.models import User
class CourseCategory(models.Model):    
    name = models.CharField(max_length=200)
    icon =  models.CharField(max_length=200)   
    def __str__(self):
        return self.name

class CourseProduct(models.Model): 
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)   
    name = models.CharField(max_length=200) 
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    is_favorited = models.CharField(max_length=200)
    description = models.CharField(max_length=200)   
    recommended = models.BooleanField(default=False)   
    featured = models.BooleanField(default=False) 
    def __str__(self):
        return self.name
    
class Lesson(models.Model): 
    course = models.ForeignKey(CourseProduct, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200) 
   
    def __str__(self):
        return self.name

class Course(models.Model):   
    name = models.CharField(max_length=200) 
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    is_favorited = models.CharField(max_length=200)
    description = models.CharField(max_length=200)      
    def __str__(self):
        return self.name
    
class Topic(models.Model):  
    course = models.ForeignKey(CourseProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic = models.CharField(max_length=100)
    content = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


     
class InProgressCourse(models.Model):
   
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
    )
    course = models.ForeignKey(CourseProduct, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField() 
    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return  "InProgressCourse: " + str(self.course.name) 
class CompletedCourse(models.Model):
   
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
    )
    course = models.ForeignKey(CourseProduct, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField() 
    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return  "CompletedCourse: " + str(self.course.name) 

# class CompletedCourse(models.Model):
#     user = models.OneToOneField(
#         User, 
#         on_delete=models.CASCADE, 
#         primary_key=True,
#         related_name='completed'
#     )
#     course = models.ForeignKey(CourseProduct, on_delete=models.CASCADE) 
#     quantity = models.PositiveIntegerField() 

#     def __str__(self):
#         return  "CompletedCourse: " + str(self.course.name) 