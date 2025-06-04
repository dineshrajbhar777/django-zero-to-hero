from django.contrib import admin
from .models import User, Invoice, Tenant

admin.site.register(User)
admin.site.register(Tenant)

class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    list_display = ["id", "invoice_number", "amount"]

admin.site.register(Invoice, InvoiceAdmin)