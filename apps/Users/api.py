from rest_framework import generics
from rest_framework import permissions
from .serializers import *


class ProfileView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserDetail(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
