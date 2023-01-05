from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from todos.serializers import TodoSerializer
from todos.models import Todo


class TodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated)

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
