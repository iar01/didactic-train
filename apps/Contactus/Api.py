from rest_framework import generics
from .serializers import *


class ContactAPI(generics.ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contactus.objects.all()