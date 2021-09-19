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
from django.urls import path
from home.views import offer_form_view, OfferListView, offer_detail_view,OfferUpdateView, OfferDeleteView
    # OfferFilterView

urlpatterns = [
    path('new/', offer_form_view, name='offercreate'),
    path('', OfferListView.as_view(), name='offerlist'),
    path('offer/<int:pk>/', offer_detail_view, name='offerdetail'),
    path('offer/update/<int:pk>/', OfferUpdateView.as_view(), name='offerupdate'),
    path('offer/del/<int:pk>/', OfferDeleteView.as_view(), name='offerdelete'),
    # path('offer_filter/', OfferFilterView.as_view(), name='offerfilter'),
]