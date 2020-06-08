from rest_framework import serializers
from .models import Framework

class FrameworkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Framework
    fields = ('id','name','type','language','url')