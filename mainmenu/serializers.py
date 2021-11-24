from .models import *
from rest_framework import serializers

class TovarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tovar
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    tovary = TovarSerializer(read_only = True, many= True)
    class Meta():
        model = Category
        fields = '__all__'