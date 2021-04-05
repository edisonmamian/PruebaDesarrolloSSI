from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


################## STATES ###################
@api_view(['GET', 'POST'])
def state_api (request):
    if request.method == 'GET':
        states = States.objects.all()
        states_serializer = StatesSerializer (states, many=True)
        return Response(states_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        states_serializer = StatesSerializer (data = request.data)
        if states_serializer.is_valid():
            states_serializer.save()
            return Response({'message': 'State created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(states_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stateDetail_api (request, pk=None):
    state = States.objects.filter(id = pk).first()

    if state:

        if request.method == 'GET':
            states_serializer = StatesSerializer(state)
            return Response(states_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            states_serializer = StatesSerializer(state, data = request.data)
            if states_serializer.is_valid():
                states_serializer.save()
                return Response ({'message': 'State updated'}, status=status.HTTP_200_OK)
            else:
                return Response (states_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            state.delete()
            return Response({'message': 'State deleted'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'State not found'}, status=status.HTTP_400_BAD_REQUEST)


################## CITIES ###################
@api_view(['GET', 'POST'])
def city_api (request):
    if request.method == 'GET':
        cities = Cities.objects.all()
        cities_serializer = CitiesSerializer (cities, many = True)
        return Response(cities_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        cities_serializer = CitiesSerializer(data = request.data)
        if cities_serializer.is_valid():
            cities_serializer.save()
            return Response({'message': 'City created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(cities_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cityDetail_api (request, pk=None):
    city = Cities.objects.filter(id=pk).first()

    if city:
        if request.method == 'GET':
            cities_serializer = CitiesSerializer(city)
            return Response(cities_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            cities_serializer = CitiesSerializer(city, data = request.data)
            if cities_serializer.is_valid():
                cities_serializer.save()
                return Response ({'message': 'City updated'}, status=status.HTTP_200_OK)
            else:
                return Response (cities_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            city.delete()
            return Response({'message': 'City deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)

################## CATEGORIES ###################
@api_view(['GET', 'POST'])
def category_api (request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer (categories, many = True)
        return Response(categories_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        categories_serializer = CategoriesSerializer(data = request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response({'message': 'Category created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoryDetail_api (request, pk=None):
    category = Categories.objects.filter(id=pk).first()

    if category:
        if request.method == 'GET':
            categories_serializer = CategoriesSerializer(category)
            return Response(categories_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            categories_serializer = CategoriesSerializer(category, data = request.data)
            if categories_serializer.is_valid():
                categories_serializer.save()
                return Response ({'message': 'Category updated'}, status=status.HTTP_200_OK)
            else:
                return Response (categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            category.delete()
            return Response({'message': 'Category deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)

################## PropertyTypes ###################
@api_view(['GET', 'POST'])
def propertyTypes_api (request):
    if request.method == 'GET':
        propertyTypes = PropertyTypes.objects.all()
        propertyTypes_serializer = PropertyTypesSerializer (propertyTypes, many = True)
        return Response(propertyTypes_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        propertyTypes_serializer = PropertyTypesSerializer(data = request.data)
        if propertyTypes_serializer.is_valid():
            propertyTypes_serializer.save()
            return Response({'message': 'Property type created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(propertyTypes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def propertyTypesDetail_api (request, pk=None):
    propertyType = PropertyTypes.objects.filter(id=pk).first()

    if propertyType:
        if request.method == 'GET':
            propertyTypes_serializer = PropertyTypesSerializer(propertyType)
            return Response(propertyTypes_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            propertyTypes_serializer = PropertyTypesSerializer(propertyType, data = request.data)
            if propertyTypes_serializer.is_valid():
                propertyTypes_serializer.save()
                return Response ({'message': 'Property type updated'}, status=status.HTTP_200_OK)
            else:
                return Response (propertyTypes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            propertyType.delete()
            return Response({'message': 'Property type deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'Property type not found'}, status=status.HTTP_400_BAD_REQUEST)

################## Transactions ###################
@api_view(['GET', 'POST'])
def Transactions_api (request):
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        transactions_serializer = TransactionsSerializer (transactions, many = True)
        return Response(transactions_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        transactions_serializer = TransactionsSerializer(data = request.data)
        if transactions_serializer.is_valid():
            transactions_serializer.save()
            return Response({'message': 'Transaction created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(transactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def TransactionsDetail_api (request, pk=None):
    transaction = Transactions.objects.filter(id=pk).first()

    if transaction:
        if request.method == 'GET':
            transactions_serializer = TransactionsSerializer(transaction)
            return Response(transactions_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            transactions_serializer = TransactionsSerializer(transaction, data = request.data)
            if transactions_serializer.is_valid():
                transactions_serializer.save()
                return Response ({'message': 'Transaction updated'}, status=status.HTTP_200_OK)
            else:
                return Response (transactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            transaction.delete()
            return Response({'message': 'Transaction deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'Transaction not found'}, status=status.HTTP_400_BAD_REQUEST)

################## Properties ###################
@api_view(['GET', 'POST'])
def Properties_api (request):
    if request.method == 'GET':
        properties = Properties.objects.all()
        properties_serializer = PropertiesSerializer (properties, many = True)
        return Response(properties_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        properties_serializer = PropertiesSerializer(data = request.data)
        if properties_serializer.is_valid():
            properties_serializer.save()
            return Response({'message': 'Property created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(properties_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def PropertiesDetail_api (request, pk=None):
    property = Properties.objects.filter(id=pk).first()

    if property:
        if request.method == 'GET':
            properties_serializer = PropertiesSerializer(property)
            return Response(properties_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            properties_serializer = PropertiesSerializer(property, data = request.data)
            if properties_serializer.is_valid():
                properties_serializer.save()
                return Response ({'message': 'Property updated'}, status=status.HTTP_200_OK)
            else:
                return Response (properties_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            property.delete()
            return Response({'message': 'Property deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'Property not found'}, status=status.HTTP_400_BAD_REQUEST)

################## Reviews ###################
@api_view(['GET', 'POST'])
def Reviews_api (request):
    if request.method == 'GET':
        reviews = Reviews.objects.all()
        review_serializer = ReviewsSerializer (reviews, many = True)
        return Response(review_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        review_serializer = ReviewsSerializer(data = request.data)
        if review_serializer.is_valid():
            review_serializer.save()
            return Response({'message': 'Review created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ReviewsDetail_api (request, pk=None):
    review = Reviews.objects.filter(id=pk).first()

    if review:
        if request.method == 'GET':
            review_serializer = ReviewsSerializer(review)
            return Response(review_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            review_serializer = ReviewsSerializer(review, data = request.data)
            if review_serializer.is_valid():
                review_serializer.save()
                return Response ({'message': 'Review updated'}, status=status.HTTP_200_OK)
            else:
                return Response (review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            review.delete()
            return Response({'message': 'Review deleted'}, status=status.HTTP_200_OK)

    else:
        return Response({'message': 'Review not found'}, status=status.HTTP_400_BAD_REQUEST)
