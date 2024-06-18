import datetime
from random import randint

from django.core.management.base import BaseCommand

from apps.employees_department.models import Department, Employee


class Command(BaseCommand):

    def handle(self, *args, **options):
        Department.objects.all().delete()
        Employee.objects.all().delete()
        for i in range(1, 5):
            department_1 = Department.objects.create(
                name=f'Отдел {i}'
            )
            for j in range(1, 2):
                department_2 = Department.objects.create(
                    name=f'Отдел {1}.{j}',
                    parent=department_1
                )
                for k in range(1, 3):
                    department_3 = Department.objects.create(
                        name=f'Отдел {1}.{j}.{k}',
                        parent=department_2
                    )
                    for d in range(1, 4):
                        department_4 = Department.objects.create(
                            name=f'Отдел {1}.{j}.{k}.{k}',
                            parent=department_3
                        )
                        for a in range(1, 1):
                            department_5 = Department.objects.create(
                                name=f'Отдел {i}.{j}.{k}.{k}.{a}',
                                parent=department_4
                            )

        departments = Department.objects.all()
        d_limit = len(departments) - 1
        employees = []

        for i in range(50000):
            employees.append(
                Employee(
                    first_name=f'Имя {i}',
                    last_name=f'Фамилия {i}',
                    fathers_name=f'Отчество {i}',
                    department=departments[randint(1, d_limit)],
                    position=f'Должность {i}',
                    monthly_salary=randint(50, 100) * 1000,
                    start_date=datetime.date(randint(2019, 2023), randint(1, 12), randint(1, 28))
                )
            )
        Employee.objects.bulk_create(employees)
