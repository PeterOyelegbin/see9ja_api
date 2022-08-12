from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('tourism-list/', views.tourismList, name='tourism-list'),
    path('tourism-detail/<str:pk>/', views.tourismDetail, name='tourism-detail'),
    path('tourism-create/', views.tourismCreate, name='tourism-create'),
    path('tourism-update/<str:pk>/', views.tourismUpdate, name='tourism-update'),
    path('tourism-delete/<str:pk>/', views.tourismDelete, name='tourism-delete'),
    
    path('tradition-list/', views.traditionList, name='tradition-list'),
    path('tradition-detail/<str:pk>/', views.traditionDetail, name='tradition-detail'),
    path('tradition-create/', views.traditionCreate, name='tradition-create'),
    path('tradition-update/<str:pk>/', views.traditionUpdate, name='tradition-update'),
    path('tradition-delete/<str:pk>/', views.traditionDelete, name='tradition-delete'),

    path('artsNculture-list/', views.artsNcultureList, name='artsNculture-list'),
    path('artsNculture-detail/<str:pk>/', views.artsNcultureDetail, name='artsNculture-detail'),
    path('artsNculture-create/', views.artsNcultureCreate, name='artsNculture-create'),
    path('artsNculture-update/<str:pk>/', views.artsNcultureUpdate, name='artsNculture-update'),
    path('artsNculture-delete/<str:pk>/', views.artsNcultureDelete, name='artsNculture-delete'),
]