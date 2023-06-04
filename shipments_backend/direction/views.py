from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Direction
from .serializers import DirectionDetailSerializer, DirectionSerializer


class DirectionAPIViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    http_method_names = ('get', 'post')

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if Direction.objects.filter(**request.data).exists():
            return Response('Direction with such params is already exists',
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DirectionSerializer
        if self.request.method == 'POST':
            return DirectionDetailSerializer
