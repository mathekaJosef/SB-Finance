from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from .models import Employee, Payslip, Customer, Sale, Expense
from django.template import RequestContext
from django.db.models import Sum

# Create your views here.
def index(request):
    pays = Payslip.objects.all()
    sales = Sale.objects.all()
    expenses = Expense.objects.all()
    context = {
        'pays': pays,
        'sales': sales,
        'expenses': expenses
    }
        
    return render(request, 'report.html', context)


def print_download(request, sale_id):
    invoices = Sale.objects.filter(pk=sale_id)
    # amounts = invoices.objects.aggregate(Sum('Amount'))
    
    context = {
        'invoices': invoices,
    }
    
    return render(request, 'print_download.html', context)

