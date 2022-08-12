from rest_framework import serializers
from .models import Tourism, Tradition, ArtsNCulture


class TourismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourism
        fields = '__all__'


class TraditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tradition
        fields = '__all__'


class ArtsNCultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsNCulture
        fields = '__all__'