from authentication import views
from django.urls import path
from todos.views import TodosApiView, TodoDetailApiView


urlpatterns = [
    path('', TodosApiView.as_view(), name="todos"),
    path("<int:id>", TodoDetailApiView.as_view(), name="todo"),
]
