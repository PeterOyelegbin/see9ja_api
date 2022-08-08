from rest_framework import serializers
from .models import Tradition


class TraditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tradition
        fields = '__all__'