from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def add_cart(request):
    data = request.data

    user_id = data["user_id"]
    user = get_user_model().objects.get(id=user_id)
    products = data["products"]
    card = None
    result = {}
    try:
        card = Card.objects.get(user=user)
    except Card.DoesNotExist:
        card = Card.objects.create(user=user)
    result = {}
    result["user_id"] = user_id
    result["cart_id"] = card.id
    result["cart_items"] = []

    for product in products:
        product_id = product["product_id"]
        total = product["total"]

        product = Tovar.objects.get(id=product_id)
        try:
            card_item = CardItem.objects.get(product=product, card=card)
            card_item.total = total

        except CardItem.DoesNotExist:
            card_item = CardItem.objects.create(
                product=product,
                card=card,
                total=total
            )
        card_item.save()
        result["cart_items"].append({"id": card_item.id, "total": card_item.total, "product": card_item.product.id})
    return JsonResponse(result)