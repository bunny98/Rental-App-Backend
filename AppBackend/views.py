from django.shortcuts import render
from AppBackend.models import RentSomething
from AppBackend.serializers import RentSomethingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ParseError
from rest_framework import status

# Create your views here.


class UploadView(APIView):
    parser_class = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        serializer = RentSomethingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        savedObjs = RentSomething.objects.all()
        serializer = RentSomethingSerializer(savedObjs, many=True)
        return Response(serializer.data)
