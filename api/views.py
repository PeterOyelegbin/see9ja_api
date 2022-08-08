from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tradition
from .serializers import TraditionSerializer


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/tradition-list/',
        'Detail View': '/tradition-detail/<str:pk>/',
        'Create': '/tradition-create/',
        'Update': '/tradition-update/<str:pk>/',
        'Delete': '/tradition-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def traditionList(request):
    tradition = Tradition.objects.all()
    serializer = TraditionSerializer(tradition, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def traditionDetail(request, pk):
    tradition = Tradition.objects.get(id=pk)
    serializer = TraditionSerializer(tradition, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def traditionCreate(request):
    serializer = TraditionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def traditionUpdate(request, pk):
    tradition = Tradition.objects.get(id=pk)
    serializer = TraditionSerializer(instance=tradition, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def traditionDelete(request, pk):
    tradition = Tradition.objects.get(id=pk)
    tradition.delete()
    return Response('Item successfully deleted!')