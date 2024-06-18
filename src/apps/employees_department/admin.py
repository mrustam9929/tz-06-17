from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter
from mptt.forms import TreeNodeChoiceField

from apps.employees_department.models import Department, Employee


class EmployeeForm(forms.ModelForm):
    department = TreeNodeChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'


@admin.register(Department)
class AdminDepartment(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = (
        'full_name', 'department', 'position', 'monthly_salary', 'start_date'
    )
    list_filter = (('department', TreeRelatedFieldListFilter),)

    form = EmployeeForm
