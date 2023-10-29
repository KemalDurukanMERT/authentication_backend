from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserMVS(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     user = self.get_object()

    # @action(detail=False, methods=["GET"])

