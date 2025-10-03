from rest_framework import serializers
from .models import Bebida

class BebidaSerializer(serializers.ModelSerializer):
    sabor_display = serializers.CharField(source='get_sabor_display', read_only=True)

    class Meta:
        model = Bebida
        fields = ['id', 'sabor', 'sabor_display', 'volumen_ml', 'precio']
