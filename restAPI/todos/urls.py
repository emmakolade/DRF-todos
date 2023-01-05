from authentication import views
from django.urls import path
from todos.views import TodosApiView


urlpatterns = [
    path('', TodosApiView.as_view(), name="todos"),
]
