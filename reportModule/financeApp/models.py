from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
import django
from django.core.validators import RegexValidator
from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.utils import timezone

class Employee(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField("first name".capitalize(), max_length=16)
    last_name = models.CharField("last name".capitalize(), max_length=16)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    date_of_birth = models.DateField("Date of Birth", default=None)

    # USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'

    def __str__(self):
        a = self.first_name
        b = self.last_name
        full_name = f'{a.capitalize()} {b.capitalize()}'
        return full_name


class Payslip(models.Model):
    Employee = models.ForeignKey(Employee, related_name='payroll', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True,)
    basic_pay = models.IntegerField(default=0, name='basic_pay')
    benefits = models.IntegerField(default=0, name='benefits')
    

class Customer(models.Model):
    customer_no = models.CharField(max_length=100)  # LLL-FFF-N
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True)
    is_company = models.BooleanField()
    PRICE_CHOICES = (
        ('R', 'Retail'),
        ('W', 'Wholesale'),
        ('D', 'Dealer'),
        ('S', 'Special'),
    )
    price_type = models.CharField(max_length=2, choices=PRICE_CHOICES, default='R')
    unit_number = models.CharField(max_length=50, blank=True, \
                                   verbose_name='House/Appt No')
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    vat_registration_number = models.IntegerField(default=0, blank=True)
    business_registration_number = models.CharField(max_length=9, blank=True)
    discount_percent = models.FloatField(default=0, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    class Meta:
        unique_together = (('first_name', 'last_name'),)
        
        
class Sale(models.Model):
    invoice_no = models.IntegerField()  # CHN starts at N=1
    date = models.DateField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    remarks = models.CharField(max_length=255, blank=True)
    requisition_number = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    Amount = models.IntegerField()


class Expense(models.Model):
    choice = (
        ('bills', 'Bills'),
        ('Payments', 'payments'),
        ('pettycash', 'Pettycash'),
        ('other', 'Other'),
    )

    Transaction_name = models.CharField(max_length=250, )
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=250, choices=choice)


    