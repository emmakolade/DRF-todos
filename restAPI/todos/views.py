from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from todos.serializers import TodoSerializer
from todos.models import Todo
from django_filters.rest_framework import DjangoFilterBackend


class TodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated)
    
    filter_backends=[DjangoFilterBackend]
    filter_fields= ['id', 'title', 'is_complete', 'description']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
