from django.shortcuts import render
from rest_framework.views import APIView

from .models import Quote
from .serializers import QuoteSerializers
