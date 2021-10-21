from rest_framework import generics
from .serializers import ShowSerializer
from .models import Show

class ShowList(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer