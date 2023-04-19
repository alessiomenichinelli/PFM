from django import forms
from .models import Expense, Balance, Payment_Method

class ExpenseForm(forms.ModelForm):
    balance = forms.ModelChoiceField(queryset=Balance.objects.none(), empty_label=None)
    payment_method = forms.ModelChoiceField(queryset=Payment_Method.objects.none(), empty_label=None)
    class Meta:
        model = Expense
        fields = ('balance', 'payment_method', 'amount', 'date', 'category', 'description',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["balance"].queryset = Balance.objects.filter(user=user)
        self.fields["payment_method"].queryset = Payment_Method.objects.filter(user=user)

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ('name',)

class PMForm(forms.ModelForm):
    class Meta:
        model = Payment_Method
        fields = ('name',)