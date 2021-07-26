from rest_framework import serializers
from concertapp.models import Performance
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['id', 'title', 'poster']
