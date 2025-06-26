from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
