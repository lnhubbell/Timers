from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Timer


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        owner = serializers.Field(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    timers = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'timers')
