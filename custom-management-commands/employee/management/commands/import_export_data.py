"""
Help:
    python.exe .\manage.py import_export_data --help
    
Import: 
    python manage.py import_export_data import --file "D:\Workspace\django-zero-to-hero\sample-data\employees.csv"

Export:
    python manage.py import_export_data export --file="D:\Workspace\django-zero-to-hero\sample-data\employees_output.csv"
"""

from django.core.management.base import BaseCommand
from employee.models import Employee
from datetime import datetime
import csv


class Command(BaseCommand):
    help = "Import or export data to/from Employee"

    def add_arguments(self, parser):
        parser.add_argument("action",
                            choices=["import", "export"],
                            help="Import or export data")
        parser.add_argument("--file",
                            type=str,
                            required=True,
                            help="Path to CSV file")

    def handle(self, *args, **options):
        action = options["action"]
        file_path = options["file"]

        if action == "import":
            print(f"Import file:= {file_path}")
            self.import_data(file_path)
        elif action == "export":
            print(f"Export file:= {file_path}")
            self.export_data(file_path)

    def import_data(self, file_path):
        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            counter = 0
            for row in reader:
                # print(f"row:= {row}")
                Employee.objects.update_or_create(
                    id = row["EMPLOYEE_ID"],
                    defaults={
                        "employee_id": row["EMPLOYEE_ID"],
                        "first_name": row["FIRST_NAME"],
                        "last_name": row["LAST_NAME"],
                        "email": row["EMAIL"],
                        "phone_number": row["PHONE_NUMBER"],
                        "hire_date": datetime.strptime(row["HIRE_DATE"], "%d-%b-%y").date(),
                        "job_id": row["JOB_ID"],
                        "salary": row["SALARY"],
                        "commission_pct": row["COMMISSION_PCT"],
                        "manager_id": row["MANAGER_ID"],
                        "department_id": row["DEPARTMENT_ID"],
                    }
                )
        self.stdout.write(self.style.SUCCESS("Data imported succesfully"))
    def export_data(self, file_path):
        with open(file_path, "w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["employee_id", "first_name", "last_name", "email", 
                          "phone_number", "hire_date", "job_id", "salary", 
                          "commission_pct", "manager_id", "department_id"]
            writes = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writes.writeheader()
            for row in Employee.objects.all().order_by("employee_id"):
                writes.writerow({
                    "employee_id": row.employee_id,
                    "first_name": row.first_name,
                    "last_name": row.last_name,
                    "email": row.email,
                    "phone_number": row.phone_number,
                    "hire_date": row.hire_date,
                    "job_id": row.job_id,
                    "salary": row.salary,
                    "commission_pct": row.commission_pct,
                    "manager_id": row.manager_id,
                    "department_id": row.department_id,
                })
        self.stdout.write(self.style.SUCCESS("Data exported successfully."))