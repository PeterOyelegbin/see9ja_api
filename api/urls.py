from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('history-list/', views.historyList, name='history-list'),
    path('history-detail/<str:pk>/', views.historyDetail, name='history-detail'),
    path('history-create/', views.historyCreate, name='history-create'),
    path('history-update/<str:pk>/', views.historyUpdate, name='history-update'),
    path('history-delete/<str:pk>/', views.historyDelete, name='history-delete'),
    
    path('tradition-list/', views.traditionList, name='tradition-list'),
    path('tradition-detail/<str:pk>/', views.traditionDetail, name='tradition-detail'),
    path('tradition-create/', views.traditionCreate, name='tradition-create'),
    path('tradition-update/<str:pk>/', views.traditionUpdate, name='tradition-update'),
    path('tradition-delete/<str:pk>/', views.traditionDelete, name='tradition-delete'),

    path('art-list/', views.artList, name='art-list'),
    path('art-detail/<str:pk>/', views.artDetail, name='art-detail'),
    path('art-create/', views.artCreate, name='art-create'),
    path('art-update/<str:pk>/', views.artUpdate, name='art-update'),
    path('art-delete/<str:pk>/', views.artDelete, name='art-delete'),
]
