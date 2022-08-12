from rest_framework import serializers
from .models import History, Tradition, Art


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class TraditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tradition
        fields = '__all__'


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = '__all__'