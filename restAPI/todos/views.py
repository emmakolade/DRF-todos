from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from todos.serializers import TodoSerializer
from todos.models import Todo
# Create your views here.


# class CreateTodoApiView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated)

#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)


# class TodoListApiView(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated)

#     def get_queryset(self):
#         return Todo.objects.filter(user=self.request.user)


class TodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
