from .models import RentSomething
from rest_framework import serializers

class RentSomethingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentSomething
        fields = '__all__'