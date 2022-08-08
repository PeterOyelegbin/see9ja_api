from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('tradition-list/', views.traditionList, name='tradition-list'),
    path('tradition-detail/<str:pk>/', views.traditionDetail, name='tradition-detail'),
    path('tradition-create/', views.traditionCreate, name='tradition-create'),
    path('tradition-update/<str:pk>/', views.traditionUpdate, name='tradition-update'),
    path('tradition-delete/<str:pk>/', views.traditionDelete, name='tradition-delete'),
]