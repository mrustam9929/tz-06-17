from django.urls import include, path
from api import views

urlpatterns = [
    path('departments/<int:pk>/employees/', views.DepartmentEmployeesListAPIView.as_view()),
    path('departments/', views.DepartmentListAPIView.as_view()),
]
