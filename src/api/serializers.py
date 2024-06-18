from rest_framework import serializers
from apps.employees_department.models import Department, Employee


class DepartmentEmployeesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id', 'first_name', 'last_name', 'position', 'monthly_salary', 'start_date'
        )


class DepartmentListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = (
            'id', 'name', 'children'
        )

    def get_children(self, obj: Department):
        return DepartmentListSerializer(obj.get_children(), many=True, context=self.context).data
