from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BundleCreate(APIView):
    serializer_class = BundleSerializer

    def get(self, request, format=None):
        data = Bundle.objects.all().order_by('Price')
        serializer = BundleDataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BundleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BundleData(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Bundle.objects.filter(id=self.kwargs['pk'])

    serializer_class = BundleSerializer
