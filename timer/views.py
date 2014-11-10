from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Timer
from .serializers import TimerSerializer, UserSerializer


class TimerList(generics.ListCreateAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        """Add owner to model prior to saving."""
        obj.owner = self.request.user


class TimerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        """Add owner to model prior to saving."""
        obj.owner = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
