from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from todos.serializers import TodoSerializer
# Create your views here.

class CreateTodoApiView(CreateAPIView):
    serializer_class=