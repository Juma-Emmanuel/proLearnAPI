from django.contrib import admin
from django.urls import path

from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
app_name = "learningapp"
urlpatterns = [
     path('user-register/', UserRegistrationView.as_view(), name='cust-registration-api'),
     path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth-refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    
    path('users/', UsersView.as_view(), name='users-list'),
    path('current-user/', UserDetailsView.as_view(), name='current-user'),
     path('logout/', LogoutView.as_view(), name='logout'),
     

     path('categories/', GetCategoryView.as_view(), name='courseproducts'), 
    path('courseproducts/', GetCourseProductsView.as_view(), name='courseproducts'),   
    path('featuredcourses/', GetFeaturedCoursesView.as_view(), name='featuredcourses'), 
    path('recommendedcourses/', GetRecommendedCoursesView.as_view(), name='recommendedcourses'), 
    path('courseproducts/<str:category_name>/', views.get_products_by_category_name, name='get_course-product_by_category_name'),
    path('courses/', GetCoursesView.as_view(), name='courses'),   
    path('courses/<int:course_id>/notes/', views.get_notes_for_course, name='get_notes_for_course'),
    path('add-to-collection/<int:course_product_id>/', AddToCollectionCourseView.as_view(), name='add-to-collection'),
    path('add-to-completed/<int:course_product_id>/', AddToCompletedCourseView.as_view(), name='add-to-completed'),
    path('lessons/<int:course_product_id>/', LessonListView.as_view(), name='lessons'),
    path('report/', ReportDetailsView.as_view(), name='report'),
    path('collectioncourses/', GetCollectionCoursesView.as_view(), name='collectioncourses'),
     path('completedcourses/', GetCompletedCoursesView.as_view(), name='completedcourses'),

]