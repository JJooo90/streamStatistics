from django.shortcuts import render
from django.http import HttpResponse

# from .serializers import ChzzkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def hello(request):
   return HttpResponse("Hello, World!")




# @api_view(['POST'])
# def create_chzzk(request):
#     serializer = ChzzkSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)