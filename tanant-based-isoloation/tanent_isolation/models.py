from django.contrib.auth.models import AbstractUser
from django.db import models

# Define Your Tenant and User Models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class User(AbstractUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    

# Create a Tenant-Aware Base Model

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
        
# Create Your Business Model (e.g., Invoice)

class Invoice(TenantAwareModel):
    invoice_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Invoice(invoice_number={self.invoice_number}, amount={self.amount})"