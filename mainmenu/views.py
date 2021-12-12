from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name']
class TovarViewSet(viewsets.ModelViewSet):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name']
class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer