from rest_framework import serializers
from .models import CardSet


# Create a serializer as a class
class CardSerializer(serializers.ModelSerializer):
    class Meta:  # Set the metadata
        model = CardSet
        fields = ('set_title', 'pub_date', 'active')
