from django.http import QueryDict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from direction.models import Direction

from .models import Shipment
from .serializers import (ShipmentCreateSerializer, ShipmentPatchSerializer,
                          ShipmentSerializer)


class ShipmentsAPIViewSet(ModelViewSet):
    queryset = Shipment.objects.select_related(
        'to_direction', 'transporter',
        )
    http_method_names = ('get', 'post', 'delete', 'patch')

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.queryset.filter(
            is_deleted=False), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        to_direction = data.pop('to_direction')
        direction = Direction.objects.filter(**to_direction)
        if direction.exists():
            direction_obj = direction.first()
        else:
            direction_obj = Direction.objects.create(**to_direction)

        data['direction_id'] = direction_obj.id

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk, *args, **kwargs):
        queryset = self.queryset.filter(is_deleted=False, pk=pk)
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk, *args, **kwargs):
        queryset = self.queryset.filter(pk=pk)
        if queryset.exists():
            shipment = queryset.first()
            shipment.is_deleted = True
            shipment.save(update_fields=['is_deleted'])
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk, *args, **kwargs):
        queryset = self.queryset.filter(pk=pk)
        if queryset.exists():
            if isinstance(request.data, QueryDict):
                data = request.data.dict()
            else:
                data = request.data
            serializer = self.get_serializer(queryset.first(),
                                             data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def get_serializer_class(self):
        if self.action in ['create']:
            return ShipmentCreateSerializer
        if self.action in ['list', 'retrieve']:
            return ShipmentSerializer
        if self.action in ['partial_update']:
            return ShipmentPatchSerializer
