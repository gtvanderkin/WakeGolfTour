from django.urls import path
from . import views

urlpatterns = [
    path('', views.GolfCourseListView.as_view(), name='golf_course_list',),
    path('<int:pk>/', views.GolfCourseDetailView.as_view(), name='golf_course_detail')
]
