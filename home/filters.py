import django_filters
from .models import *


class OfferFilter(django_filters.FilterSet):
    class Meta:
        model = Offer
        fields = ['negotiable', 'size_category', 'maintenance_category',
                  'indoor', 'outdoor', 'pet_friendly', 'location']
