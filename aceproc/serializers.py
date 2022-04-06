from rest_framework import serializers
from .models import Card


# Create a serializer as a class
class CardSerializer(serializers.ModelSerializer):
    class Meta:  # Set the metadata
        model = Card
        fields = (
            'question_text', 'answer_text', 'created_date', 'rel_cardset'
        )
