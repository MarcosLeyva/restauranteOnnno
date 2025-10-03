from django.urls import path
from .views import BebidaListCreateAPIView, BebidaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('bebidas/', BebidaListCreateAPIView.as_view(), name='bebida-list-create'),
    path('bebidas/<int:pk>/', BebidaRetrieveUpdateDestroyAPIView.as_view(), name='bebida-detail'),
]
