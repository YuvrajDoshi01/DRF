from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer

class UserSetView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupSetView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


