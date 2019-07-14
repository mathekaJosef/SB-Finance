from django.contrib import admin

from .models import Employee, Payslip, Customer, Expense, Sale

admin.site.register(Employee)
admin.site.register(Payslip)
admin.site.register(Customer)
admin.site.register(Expense)
admin.site.register(Sale)