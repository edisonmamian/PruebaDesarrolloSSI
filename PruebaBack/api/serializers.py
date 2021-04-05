from rest_framework import serializers
from .models import *

class StatesSerializer (serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'

class CitiesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

class CategoriesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class TransactionsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'

class PropertiesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'

class PropertyTypesSerializer (serializers.ModelSerializer):
    class Meta:
        model = PropertyTypes
        fields = '__all__'

class ReviewsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
