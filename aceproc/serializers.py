from rest_framework import serializers
from .models import Card, CardSet


# Create a serializer as a class
class CardSerializer(serializers.ModelSerializer):
    class Meta:  # Set the metadata
        model = Card
        fields = (
            'question_text', 'answer_text', 'created_date', 'rel_cardset'
        )

# Returns all the parent cardsets
class CardSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardSet
        fields = (
            'set_title', 'pub_date', 'active'
        )