from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('new/', views.expense_new, name ='expense_new'),
    path('expense/<int:pk>/', views.expense_show, name='expense_show'),
    path('edit/<int:pk>/', views.expense_edit, name='expense_edit'),
    path('delete/<int:pk>/', views.expense_delete, name='expense_delete'),
    path('new_bal/', views.balance_new, name ='balance_new'),
    path('new_pm/', views.payment_method_new, name ='payment_method_new'),
    path('api/balances/', views.BalancesAPI.as_view(), name = 'balances_api'),
    path('api/pm/', views.PMAPI.as_view(), name = 'pm_api')
]