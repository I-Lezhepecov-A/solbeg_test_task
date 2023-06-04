from django.http import QueryDict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Transporter
from .serializers import TransporterDetailSerializer, TransporterSerializer


class TransportersAPIViewSet(ModelViewSet):
    queryset = Transporter.objects.all()
    http_method_names = ('get', 'post')

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if Transporter.objects.filter(**request.data).exists():
            return Response('Transporter with such params is already exists',
                            status=status.HTTP_400_BAD_REQUEST)
        if isinstance(request.data, QueryDict):
            data = request.data.dict()
        else:
            data = request.data
        serializer = self.get_serializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransporterSerializer
        if self.request.method == 'POST':
            return TransporterDetailSerializer
