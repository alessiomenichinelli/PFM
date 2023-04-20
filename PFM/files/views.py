import csv
from django.shortcuts import render, get_object_or_404 ,redirect
from expenses.models import Expense, Balance, Payment_Method, Category
from .models import File

def LoadFile(request, pk):
    file = open("./uploads/expenses.txt", "r")
    expenses = file.readlines()
    for expense in expenses:
        row = expense.rstrip().split(",")
        e = Expense(user=request.user, balance=Balance.objects.get(name=row[1]), payment_method=Payment_Method.objects.get(name=row[2]), amount=float(row[3]), date=row[4], category=Category.objects.get(name=row[5]), description=row[6])
        e.save()
    return redirect('expenses_list')