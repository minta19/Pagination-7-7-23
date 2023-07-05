from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BooklistCreate(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def delete(self, request, *args, **kwargs):
        response= super().delete(request, *args, **kwargs)
        return Response({"message":"Book Deleted !!"})
