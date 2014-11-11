# from django.forms import widgets
from rest_framework import serializers
from .models import Timer


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
