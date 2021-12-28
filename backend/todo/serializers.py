from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed')