from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OfferSerializer, Offer


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {'Create': 'new/',
                'List': '',
                'Detail': 'offer/<int:pk>/',
                'Update': 'offer/update/<int:pk>/',
                'Delete': 'offer/del/<int:pk>/',
                }
    return Response(api_urls)


@api_view(['GET'])
def offer_list(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def offer_detail(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(offer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def offer_create(request):
    serializer = OfferSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def offer_update(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(instance=offer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def offer_delete(request, pk):
    offer = Offer.objects.get(id=pk)
    offer.delete()
    return Response('Offer deleted!')
