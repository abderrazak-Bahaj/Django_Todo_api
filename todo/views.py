from django.shortcuts import render
from rest_framework import response
from .serializer import TodoItemSerializer
from .models import TodoItem
#resr framework view api
from rest_framework.views import APIView

class TodoView(APIView):
    def get(self,request):
        todo_list = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_list,many=True,context={'request':request})
        return response.Response({"message":serializer.data},status=200)
    