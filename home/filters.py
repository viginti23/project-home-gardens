import django_filters
from .models import *
from django_filters import DateFilter, CharFilter, NumberFilter
from django.forms.widgets import TextInput, NumberInput, DateInput, SelectDateWidget


class TitleFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Nazwa produktu',
                       widget=TextInput(attrs={
                           'placeholder': "Znajdź swoją roślinę!",
                           'class': "form-control me-2 button-search-right"}))

    class Meta:
        model = Offer
        fields = ['title']


class OfferFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_posted', lookup_expr='gte', label='Data od:',
                            widget=SelectDateWidget(empty_label=('rok', 'miesiąc', 'dzień'), attrs={
                                'class': "form-control me-2 button-search-right",
                                'style': 'width: auto; display: inline-block;'}))
    end_date = DateFilter(field_name='date_posted', lookup_expr='lte', label='Data do:',
                          widget=SelectDateWidget(empty_label=('rok', 'miesiąc', 'dzień'), attrs={
                              'class': "form-control me-2 button-search-right",
                              'style': 'width: auto; display: inline-block;'}))

    cheapest = NumberFilter(field_name='price', lookup_expr='gte', label='Cena od',
                            widget=NumberInput(attrs={
                                'class': "form-control me-2 button-search-right",
                                'style': 'width: auto; display: inline-block; margin: 4px'}))

    expensive = NumberFilter(field_name='price', lookup_expr='lte', label='Cena do',
                             widget=NumberInput(attrs={
                                 'class': "form-control me-2 button-search-right",
                                 'style': 'width: auto; display: inline-block; margin: 4px'}))

    class Meta:
        model = Offer
        fields = '__all__'
        exclude = ['seller', 'description', 'date_posted', 'title', 'price', ]
