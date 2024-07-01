from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'title', 'body']