import re

from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quote
from .serializers import QuoteSerializers
import requests


class QuoteListAPIView(APIView):
    def get(self, request):
        quote = Quote.objects.all()
        serializers = QuoteSerializers(quote, many=True)
        return Response(serializers.data)


class QuoteAPIView(APIView):

    def get(self, request):
        data = Quote.objects.all()
        quote = requests.get('https://api.kanye.rest/')
        quote = quote.json()
        quote = quote['quote']
        lower = 0
        upper = 0
        for i in quote:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            else:
                continue
        vowel = 0
        consonants = 0
        for i in quote:
            if i in 'eyuioaEYUIOA':
                vowel+=1
            elif i in 'qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM':
                consonants+=1
        quote_db = Quote.objects.create(
            name=quote,
            len_of_quote=len(quote),
            upper=upper,
            lower=lower,
            vowel=vowel,
            consonants=consonants
        )
        quote_db.save()
        return Response(quote)


class QuoteDetailAPIView(APIView):

    def get_object(self, id):
        try:
            return Quote.objects.get(id=id)
        except Quote.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
