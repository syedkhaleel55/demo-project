from django.shortcuts import render

# Create your views here.
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import *  
from .serializers import *  
from django.shortcuts import get_object_or_404  
# Create your views here.  
  
class BookView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Book.objects.all()  
        serializers = BookSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = BookSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    def patch(self, request, id):  
        result = Book.objects.get(id=id)  
        serializer = BookSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors}) 
    def delete(self, request, id=None):  
        result = get_object_or_404(Book, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  
              