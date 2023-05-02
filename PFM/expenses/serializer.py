from rest_framework import serializers
from .models import User, Profile, Balance, Payment_Method, Category, Expense

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class BalanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

class PMSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment_Method
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'