from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import OfferSerializer, Offer


# Create your views here.
@permission_classes([AllowAny,])
@api_view(['GET'])
def apiOverview(request):
    api_urls = {'Create': 'offer-create/',
                'List': 'offer-list',
                'Detail': 'offer/<int:pk>/',
                'Update': 'offer/update/<int:pk>/',
                'Delete': 'offer/del/<int:pk>/',
                }
    return Response(api_urls)


@permission_classes([AllowAny,])
@api_view(['GET'])
def offer_list(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)


@permission_classes([AllowAny,])
@api_view(['GET'])
def offer_detail(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(offer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def offer_create(request):
    serializer = OfferSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def offer_update(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(instance=offer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def offer_delete(request, pk):
    offer = Offer.objects.get(id=pk)
    offer.delete()
    return Response('Offer deleted!')
