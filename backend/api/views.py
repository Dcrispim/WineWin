from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import ( 
                            WineSerializer,ReviewSerializer
                        )

import json



# Create your views here.
class WineViewSet(APIView):
    serializer_class = WineSerializer
    queryset = Wine.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        
        if pk == None:
            wine = Wine.objects.all()
            serializer = WineSerializer(wine, many=True)
        else:
            try:
                wine = Wine.objects.get(pk=pk)
                serializer = WineSerializer(wine)
            except:
                return Response(404)

        return Response(serializer.data)

class ReviewViewSet(APIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'pk'

    def get(self, request, pk=None):
        
        if pk == None:
            review = Review.objects.all()
            serializer = ReviewSerializer(review, many=True)
        else:
            try:
                review = Review.objects.get(pk=pk)
                serializer = ReviewSerializer(review)
            except:
                return Response(404)

        return Response(serializer.data)

