from .models import *
from rest_framework import serializers

class TovarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tovar
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    tovary = TovarSerializer(read_only=True, many=True)
    class Meta():
        model = Category
        fields = '__all__'


class CardItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = CardItem
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    carditems = CardItemSerializer(read_only=True, many=True)

    class Meta():
        model = Card
        fields = '__all__'