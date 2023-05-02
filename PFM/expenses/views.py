from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense, Balance, Payment_Method
from .forms import ExpenseForm, BalanceForm, PMForm
from .permissions import TelegramAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializers, ProfileSerializers, BalanceSerializers, PMSerializers ,CategorySerializers, ExpenseSerializers
from rest_framework.views import APIView
from rest_framework.response import Response

@login_required
def index(request):
    balances = Balance.objects.filter(user=request.user)
    payment_methods = Payment_Method.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user).order_by("-date")[:5]
    return render(request, 'index.html', {'balances': balances, 'payment_methods': payment_methods, 'expenses':expenses})

@login_required
def expenses_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by("-date")
    return render(request, 'expenses_list.html', {'expenses': expenses})

@login_required
def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.user, request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses_list')
    else:
        form = ExpenseForm(request.user)
    return render(request, 'expense_new.html', {'form': form})

@login_required
def expense_show(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    return render(request, 'expense_show.html', {'expense': expense})

@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == "POST":
        form = ExpenseForm(request.user, request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses_list')
    else:
        form = ExpenseForm(request.user, instance=expense)
    return render(request, 'expense_edit.html', {'form': form})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect('expenses_list')

@login_required
def balance_new(request):
    if request.method == "POST":
        form = BalanceForm(request.POST)
        if form.is_valid():
            balance = form.save(commit=False)
            balance.user = request.user
            balance.save()
            return redirect('index')
    else:
        form = BalanceForm(request.POST)
    return render(request, 'balance_new.html', {'form': form})

@login_required
def payment_method_new(request):
    if request.method == "POST":
        form = PMForm(request.POST)
        if form.is_valid():
            pm = form.save(commit=False)
            pm.user = request.user
            pm.save()
            return redirect('index')
    else:
        form = BalanceForm(request.POST)
    return render(request, 'payment_method_new.html', {'form': form})

class BalancesAPI(APIView):
    authentication_classes = [TelegramAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        balances = Balance.objects.filter(user=self.request.user)
        serializer = BalanceSerializers(balances, many=True)
        bals = serializer.data
        for bal in bals:
            balance = Balance.objects.get(pk=bal['id'])
            bal['amount']=balance.calculate()
        return Response(bals)
    
class PMAPI(APIView):
    authentication_classes = [TelegramAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        pm = Payment_Method.objects.filter(user=self.request.user)
        serializer = PMSerializers(pm, many=True)
        bals = serializer.data
        for bal in bals:
            balance = Payment_Method.objects.get(pk=bal['id'])
            bal['amount']=balance.calculate()
        return Response(bals)
    