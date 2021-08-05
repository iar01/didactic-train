from requests import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class SubscriptionCheckAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            obj = queryset.get(user=self.request.user)
            self.check_object_permissions(self.request, obj)
            return obj
        except:
            raise Http404


class SubscriptionCreateView(APIView):
    serializer_class = SubscriptionCreateSerializer

    def get(self, request, format=None):
        snippets = Subscription.objects.all()
        serializer = SubscriptionSerializer(snippets, many=True)
        return Response({"data": serializer.data, })

    def post(self, request, format=None):
        print(request.data, "a")

        serializer = SubscriptionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDataView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = Subscription.objects.filter(id=self.kwargs["pk"])
        return queryset

    serializer_class = SubscriptionSerializer
