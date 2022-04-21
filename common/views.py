from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.
class RegisterAPIView(APIView):
    def post(self, requet):
        return Response("Hello")
