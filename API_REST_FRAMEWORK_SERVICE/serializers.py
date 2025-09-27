from rest_framework import serializers
from .models import Products_Fake

class ProductsFakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Fake
        fields = '__all__'