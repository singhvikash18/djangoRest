from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .serializers import EmplyoeeSerializers
from .models import Emplyoee
from .pagination import CustomPagination

class EmplyoeeRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmplyoeeSerializers

    def get_queryset(self , pk):
        try:
            emplyoee = Emplyoee.objects.get(pk=pk)
        except Emplyoee.DoesNotExist:
            content ={
                'message' : 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        return emplyoee

    #
    def get(self, request, pk):
        emplyoee =self.get_queryset(pk)
        serializer = EmplyoeeSerializers(emplyoee)

        return Response(serializer.data , status=status.HTTP_200_OK)

    #
    def put(self,request,pk):
        emplyoee = self.get_queryset(pk)
        serializer = EmplyoeeSerializers(emplyoee , data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    #
    def delete(self,request,pk):
        emplyoee = self.get_queryset(pk)
        emplyoee.delete()
        content ={
            'message':'data was deleted'
        }

        return Response(content, status=status.HTTP_204_NO_CONTENT)

class EmplyoeeView(generics.ListCreateAPIView):
    serializer_class =EmplyoeeSerializers
    pagination_class =CustomPagination


    def get_queryset(self):
        emplyoees =Emplyoee.objects.all()

        return emplyoees
   

    def get(self,request):
        emplyoees =self.get_queryset()

        # pagination
        paginate_queryset = self.paginate_queryset( emplyoees)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = EmplyoeeSerializers(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    


