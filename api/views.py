from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import History, Tradition, Art
from .serializers import HistorySerializer, TraditionSerializer, ArtSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'History List': '/history-list/',
        'History Details': '/history-detail/<str:pk>/',
        'History Create': '/history-create/',
        'History Update': '/history-update/<str:pk>/',
        'History Delete': '/history-delete/<str:pk>/',

        'Tradition List': '/tradition-list/',
        'Tradition Details': '/tradition-detail/<str:pk>/',
        'Tradition Create': '/tradition-create/',
        'Tradition Update': '/tradition-update/<str:pk>/',
        'Tradition Delete': '/tradition-delete/<str:pk>/',

        'Art List': '/art-list/',
        'Art Details': '/art-detail/<str:pk>/',
        'Art Create': '/art-create/',
        'Art Update': '/art-update/<str:pk>/',
        'Art Delete': '/art-delete/<str:pk>/',
    }
    return Response(api_urls, status=status.HTTP_200_OK)


#  Tourism view functions
@csrf_exempt
@api_view(['GET'])
def historyList(request):
    history = History.objects.all()
    serializer = HistorySerializer(history, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def historyDetail(request, pk):
    history = History.objects.get(id=pk)
    serializer = HistorySerializer(history, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def historyCreate(request):
    serializer = HistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data created successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['POST'])
def historyUpdate(request, pk):
    history = History.objects.get(id=pk)
    serializer = HistorySerializer(instance=history, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data updated successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['DELETE'])
def historyDelete(request, pk):
    history = History.objects.get(id=pk)
    history.delete()
    return Response('Data successfully deleted!', status=status.HTTP_200_OK)
    

# Tradition view functions
@csrf_exempt
@api_view(['GET'])
def traditionList(request):
    tradition = Tradition.objects.all()
    serializer = TraditionSerializer(tradition, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def traditionDetail(request, pk):
    tradition = Tradition.objects.get(id=pk)
    serializer = TraditionSerializer(tradition, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def traditionCreate(request):
    serializer = TraditionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data created successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['POST'])
def traditionUpdate(request, pk):
    tradition = Tradition.objects.get(id=pk)
    serializer = TraditionSerializer(instance=tradition, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data updated successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['DELETE'])
def traditionDelete(request, pk):
    tradition = Tradition.objects.get(id=pk)
    tradition.delete()
    return Response('Data successfully deleted!', status=status.HTTP_200_OK)
    

# Art view functions
@csrf_exempt
@api_view(['GET'])
def artList(request):
    art = Art.objects.all()
    serializer = ArtSerializer(art, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def artDetail(request, pk):
    art = Art.objects.get(id=pk)
    serializer = ArtSerializer(art, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def artCreate(request):
    serializer = ArtSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data created successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['POST'])
def artUpdate(request, pk):
    art = Art.objects.get(id=pk)
    serializer = ArtSerializer(instance=art, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Data updated successfully', status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
@api_view(['DELETE'])
def artDelete(request, pk):
    art = Art.objects.get(id=pk)
    art.delete()
    return Response('Data successfully deleted!', status=status.HTTP_200_OK)
