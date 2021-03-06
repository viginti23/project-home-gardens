"""HomeGarden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import apiOverview, offer_list, offer_create, offer_detail, offer_delete, offer_update
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('obtain-token/', obtain_auth_token, name='api-obtain-token'),
    path('', apiOverview, name='api-overview'),
    path('offer-list/', offer_list, name='api-offer-list'),
    path('offer-create/', offer_create, name='api-offer-create'),
    path('offer/<int:pk>/', offer_detail, name='api-offer-detail'),
    path('offer/update/<int:pk>/', offer_update, name='api-offer-update'),
    path('offer/del/<int:pk>/', offer_delete, name='api-offer-delete'),
]
