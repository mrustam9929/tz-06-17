from mptt.utils import get_cached_trees
from rest_framework import generics, status, permissions
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from api import serializers
from apps.employees_department.models import Employee, Department


class DepartmentEmployeesListAPIView(generics.ListAPIView):
    """Список сотрудников отдела"""
    serializer_class = serializers.DepartmentEmployeesListSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Employee.objects.filter(
            department_id=self.kwargs['pk']
        )


class DepartmentListAPIView(generics.ListAPIView):
    """Список отделов"""
    serializer_class = serializers.DepartmentListSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        # return Department.objects.filter(parent__isnull=True).get_cached_trees()  # что-то не так с методом
        return Department.objects.filter(parent__isnull=True)
