from django.contrib import admin

from .models import Balance, Payment_Method, Expense, Category

admin.site.register(Balance)
admin.site.register(Payment_Method)
admin.site.register(Expense)
admin.site.register(Category)
