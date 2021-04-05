"""PruebaBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from api.api import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('states/', state_api, name = 'states'),
    path('states/<int:pk>', stateDetail_api, name = 'states_detail'),
    path('cities/', city_api, name = 'cities'),
    path('cities/<int:pk>', cityDetail_api, name = 'cities_detail'),
    path('categories/', category_api, name = 'categories'),
    path('categories/<int:pk>', categoryDetail_api, name = 'categories_detail'),
    path('propertyTypes/', propertyTypes_api, name = 'propertyTypes'),
    path('propertyTypes/<int:pk>', propertyTypesDetail_api, name = 'propertyTypes_detail'),
    path('transactions/', Transactions_api, name = 'transactions'),
    path('transactions/<int:pk>', TransactionsDetail_api, name = 'transactions_detail'),
    path('properties/', Properties_api, name = 'properties'),
    path('properties/<int:pk>', PropertiesDetail_api, name = 'properties_detail'),
    path('reviews/', Reviews_api, name = 'reviews'),
    path('reviews/<int:pk>', ReviewsDetail_api, name = 'reviews_detail'),
]
