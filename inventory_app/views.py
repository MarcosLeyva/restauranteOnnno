from django.shortcuts import render
from rest_framework import generics
from .models import Bebida
from .serializers import BebidaSerializer

# Create your views here.

class BebidaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer

class BebidaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer
