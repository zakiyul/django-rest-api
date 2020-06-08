from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import FrameworkSerializer
from .models import Framework


class FrameworkView(viewsets.ModelViewSet):
  queryset = Framework.objects.all()
  serializer_class = FrameworkSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
