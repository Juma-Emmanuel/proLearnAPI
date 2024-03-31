from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
class UserRegistrationView(generics.CreateAPIView):
   
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        # {'username': user.username, 'email': user.email},
        return Response({}, status=status.HTTP_201_CREATED)
class UsersView(APIView):    

    def get(self, request):
        
        users = User.objects.filter(is_staff=False)
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def perform_create(self, serializer):
        return serializer.save()

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
       
        user = request.user

        # currentUser = User.objects.get(user=request.user)

        serializer = UserSerializer(user)

       
        return Response(serializer.data)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
       
        request.auth.delete()  
        
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
  
class GetCategoryView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        categories = CourseCategory.objects.all()
        serializer = CourseCategorySerializer(categories, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
class GetCourseProductsView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        courses = CourseProduct.objects.all()
        serializer = CourseProductSerializer(courses, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)


def get_products_by_category_name(request, category_name):
    try:
        category = CourseCategory.objects.get(name=category_name)
    except CourseCategory.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    courses = CourseProduct.objects.filter(category=category)
    serializer = CourseProductSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)

class GetFeaturedCoursesView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        courses = CourseProduct.objects.filter(featured=True)
        serializer = CourseProductSerializer(courses, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

class GetRecommendedCoursesView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        courses = CourseProduct.objects.filter(recommended=True)
        serializer = CourseProductSerializer(courses, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
# def get_products_by_bool_value(request, category_name):
#     try:
#         category = CourseCategory.objects.get(name=category_name)
#     except CourseCategory.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status=404)

#     courses = CourseProduct.objects.filter(category=category)
#     serializer = CourseProductSerializer(courses, many=True)
#     return JsonResponse(serializer.data, safe=False)

class GetCoursesView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

def get_lessons_for_course(request, course_id):   
    notes = Note.objects.filter(topic__course_id=course_id)    
    serializer = GetNoteSerializer(notes, many=True) 
    return JsonResponse(serializer.data, safe=False)


def get_notes_for_course(request, course_id):   
    notes = Note.objects.filter(topic__course_id=course_id)    
    serializer = GetNoteSerializer(notes, many=True) 
    return JsonResponse(serializer.data, safe=False)


class AddToCompletedCourseView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, course_product_id):
        user = request.user
        course_product = get_object_or_404(CourseProduct, id=course_product_id)
        
        # Check if the course already exists in CompletedCourse for the user
        if CompletedCourse.objects.filter(user=user, course=course_product).exists():
            return Response({'detail': 'Course already completed by the user'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new CompletedCourse entry for the user
        completed_course = CompletedCourse.objects.create(user=user, course=course_product, quantity=1)
        inprogress_course= InProgressCourse.objects.filter(course=course_product)
        inprogress_course.delete()
        # Serialize the completed_course object
        serializer = CompletedCourseSerializer(completed_course)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class GetCompletedCoursesView(APIView):
    permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        completed_courses = CompletedCourse.objects.filter(user=request.user)
        course_products = [completed.course for completed in completed_courses]
       
        serializer = CourseProductSerializer(course_products, many= True)
     
        return Response(serializer.data,status=status.HTTP_200_OK)

class AddToCollectionCourseView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, course_product_id):
        user = request.user
        course_product = get_object_or_404(CourseProduct, id=course_product_id)
        
        # Check if the course already exists in CompletedCourse for the user
        if InProgressCourse.objects.filter(user=user, course=course_product).exists():
            return Response({'detail': 'Course already collection by the user'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new CollectionCourse entry for the user
        collection_course = InProgressCourse.objects.create(user=user, course=course_product, quantity=1)
        
        # Serialize the collection_course object
        serializer = CollectionCourseSerializer(collection_course)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class GetCollectionCoursesView(APIView):
    permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        collection_courses = InProgressCourse.objects.filter(user=request.user)
        course_products = [collection.course for collection in collection_courses]
       
        serializer = CourseProductSerializer(course_products, many= True)
     
        return Response(serializer.data,status=status.HTTP_200_OK)


    
class LessonListView(APIView):
    
    def get(self, request, course_product_id, format=None):
        
        lessons = Lesson.objects.filter(course_id=course_product_id)
        
        
        serializer = LessonSerializer(lessons, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReportDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):

            
       
       
        user = request.user
               
        collection_courses = InProgressCourse.objects.filter(user=request.user)
        collection_course_count = collection_courses.count() or 0

              
        completed_courses = CompletedCourse.objects.filter(user=request.user)
        completed_course_count = completed_courses.count() or 0        
        firstName = user.first_name
        lastName = user.last_name
        date_joined = user.date_joined
        formatted_date = user.date_joined.strftime('%Y-%m-%d')
        report_data = {
            'completed_courses': completed_course_count,
            'in_progress_courses': collection_course_count,
            'first_name': firstName,
            'last_name': lastName,
            'date_joined': formatted_date,
        }
       
        
        return Response(report_data, status=status.HTTP_200_OK)

