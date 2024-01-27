from rest_framework import serializers, validators
from django.contrib.auth.hashers import make_password
from . models import *


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    class Meta:
        model = Message
        fields = '__all__'
