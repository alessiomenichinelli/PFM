from django.contrib import admin

from .models import Profile, Balance, Payment_Method, Expense, Category

admin.site.register(Profile)
admin.site.register(Balance)
admin.site.register(Payment_Method)
admin.site.register(Expense)
admin.site.register(Category)
