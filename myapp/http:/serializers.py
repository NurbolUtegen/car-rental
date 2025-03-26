from rest_framework import serializers
from .models import Car, Rental

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '_all_'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '_all_'
