from rest_framework import generics
from .models import Timer
from .serializers import TimerSerializer


class TimerList(generics.ListCreateAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer


class TimerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
