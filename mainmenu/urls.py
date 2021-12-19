from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('carditem', CardItemViewSet)
router.register('card', CardViewSet)
router.register('tovar', TovarViewSet)
router.register('category', CategoryViewSet)
router.register('add_cart', add_cart)
urlpatterns = [
    path('', include(router.urls)),
]