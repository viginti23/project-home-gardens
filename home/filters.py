import django_filters
from .models import *


class OfferFilter(django_filters.FilterSet):
    class Meta:
        model = Offer
        fields = '__all__'