from rest_framework import serializers

from direction.models import Direction
from direction.serializers import (DirectionDetailSerializer,
                                   DirectionSerializer)

from .models import Transporter


class TransporterSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    residence = DirectionDetailSerializer()

    class Meta:
        model = Transporter
        fields = (
            'id',
            'name',
            'phone',
            'residence'
        )


class TransporterDetailSerializer(TransporterSerializer):
    id = serializers.IntegerField(read_only=True)
    residence = DirectionSerializer(read_only=True)
    residence_id = serializers.PrimaryKeyRelatedField(
        source='residence',
        queryset=Direction.objects.all(),
        write_only=True
    )

    class Meta:
        model = Transporter
        fields = (
            'id',
            'name',
            'phone',
            'residence',
            'residence_id',
        )


class TransporterWithoutResidenceSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = Transporter
        fields = (
            'id',
            'name',
            'phone',
        )
