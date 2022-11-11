from rest_framework import serializers
from .models import Quote


class QuoteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ['id', 'name', 'len_of_quote', 'upper', 'lower', 'vowel', 'consonants']
