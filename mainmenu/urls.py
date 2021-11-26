from django.urls import path
from .views import *
urlpatterns = [
    path('category', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),
    path('tovar', TovarListView.as_view()),
    path('tovar/<int:pk>', TovarDetailView.as_view()),
    path('zakaz')
]