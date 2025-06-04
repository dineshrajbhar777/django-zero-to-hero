from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField(auto_now_add=True)
    job_id = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,
                                 decimal_places=4,
                                 validators=[
                                     MinLengthValidator(0.0),
                                     MaxLengthValidator(10)
                                 ])
    commission_pct = models.CharField(max_length=15)
    manager_id = models.CharField(max_length=15)
    department_id =models.CharField(max_length=15)
