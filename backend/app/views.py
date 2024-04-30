from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import React
from .serializer import ReactSerializer

class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        output = [{"food": output.food, "ingredient": output.ingredient}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)