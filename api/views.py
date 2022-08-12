from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import Tourism, Tradition, ArtsNCulture
from .serializers import TourismSerializer, TraditionSerializer, ArtsNCultureSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Tourism List': '/tourism-list/',
        'Tourism Details': '/tourism-detail/<str:pk>/',
        'Tourism Create': '/tourism-create/',
        'Tourism Update': '/tourism-update/<str:pk>/',
        'Tourism Delete': '/tourism-delete/<str:pk>/',

        'Tradition List': '/tradition-list/',
        'Tradition Details': '/tradition-detail/<str:pk>/',
        'Traditon Create': '/tradition-create/',
        'Tradition Update': '/tradition-update/<str:pk>/',
        'Tradition Delete': '/tradition-delete/<str:pk>/',

        'ArtsNCulture List': '/artsNculture-list/',
        'ArtsNCulture Details': '/artsNculture-detail/<str:pk>/',
        'ArtsNCulture Create': '/artsNculture-create/',
        'ArtsNCulture Update': '/artsNculture-update/<str:pk>/',
        'ArtsNCulture Delete': '/artsNculture-delete/<str:pk>/',
    }
    return Response(api_urls)


#  Tourism view functions
@csrf_exempt
@api_view(['GET'])
def tourismList(request):
    tourism = Tourism.objects.all()
    serializer = TourismSerializer(tourism, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def tourismDetail(request, pk):
    tourism = Tourism.objects.get(id=pk)
    serializer = TourismSerializer(tourism, many=False)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def tourismCreate(request):
    serializer = TourismSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def tourismUpdate(request, pk):
    tourism = Tourism.objects.get(id=pk)
    serializer = TourismSerializer(instance=tourism, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
@api_view(['DELETE'])
def tourismDelete(request, pk):
    tourism = Tourism.objects.get(id=pk)
    tourism.delete()
    return Response('Item successfully deleted!')
    

# Tradition view functions
@csrf_exempt
@api_view(['GET'])
def traditionList(request):
    tradition = Tradition.objects.all()
    serializer = TraditionSerializer(tradition, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def traditionDetail(request, pk):
    tradition = Tradition.objects.get(id=pk)
    serializer = TraditionSerializer(tradition, many=False)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def traditionCreate(request):
    serializer = TraditionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def traditionUpdate(request, pk):
    tradition = Tradition.objects.get(id=pk)
    serializer = TraditionSerializer(instance=tradition, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
@api_view(['DELETE'])
def traditionDelete(request, pk):
    tradition = Tradition.objects.get(id=pk)
    tradition.delete()
    return Response('Item successfully deleted!')
    

# ArtsNCulture view functions
@csrf_exempt
@api_view(['GET'])
def artsNcultureList(request):
    artsNculture = ArtsNCulture.objects.all()
    serializer = ArtsNCultureSerializer(artsNculture, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def artsNcultureDetail(request, pk):
    artsNculture = ArtsNCulture.objects.get(id=pk)
    serializer = ArtsNCultureSerializer(artsNculture, many=False)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def artsNcultureCreate(request):
    serializer = ArtsNCultureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def artsNcultureUpdate(request, pk):
    artNculture = ArtsNCulture.objects.get(id=pk)
    serializer = ArtsNCultureSerializer(instance=artNculture, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
@api_view(['DELETE'])
def artsNcultureDelete(request, pk):
    artNculture = ArtsNCulture.objects.get(id=pk)
    artNculture.delete()
    return Response('Item successfully deleted!')