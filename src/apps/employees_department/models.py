from django.db import models
from mptt.models import MPTTModel


class Department(MPTTModel):
    name = models.CharField(
        max_length=255, verbose_name='Название отдела'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
        verbose_name='Отдел'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'departments'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(
        max_length=255, verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255, verbose_name='Фамилия'
    )
    fathers_name = models.CharField(
        max_length=255, verbose_name='Отчество'
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='employees'
    )
    position = models.CharField(
        max_length=255, verbose_name='Должность'
    )
    monthly_salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Месячная зарплата'
    )
    start_date = models.DateField()

    class Meta:
        db_table = 'employees'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.fathers_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.fathers_name}'

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name, self.fathers_name = value.split()
