from django.utils import timezone
from rest_framework import serializers

from direction.models import Direction
from direction.serializers import DirectionDetailSerializer
from transporter.models import Transporter
from transporter.serializers import TransporterWithoutResidenceSerializer

from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    code = serializers.CharField()
    estimated_arrival_date = serializers.DateField()
    overdue = serializers.SerializerMethodField(read_only=True)
    sent_date = serializers.DateField()
    is_arrived = serializers.BooleanField()
    to_direction = DirectionDetailSerializer()
    transporter = TransporterWithoutResidenceSerializer()

    class Meta:
        model = Shipment
        fields = (
            'id',
            'code',
            'estimated_arrival_date',
            'overdue',
            'sent_date',
            'is_arrived',
            'to_direction',
            'transporter',
        )

    def get_overdue(self, obj: Shipment):
        if not obj.is_arrived:
            if (obj.estimated_arrival_date - timezone.now().date()).days <= 0:
                return True
        return False


class ShipmentCreateSerializer(serializers.ModelSerializer):

    estimated_arrival_date = serializers.DateField()
    sent_date = serializers.DateField()
    direction_id = serializers.PrimaryKeyRelatedField(
        source='to_direction',
        queryset=Direction.objects.all(),
        write_only=True
    )
    transporter_id = serializers.PrimaryKeyRelatedField(
        source='transporter',
        queryset=Transporter.objects.all(),
        write_only=True
    )
    to_direction = DirectionDetailSerializer(read_only=True)
    transporter = TransporterWithoutResidenceSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = (
            'id',
            'code',
            'estimated_arrival_date',
            'overdue',
            'sent_date',
            'is_arrived',
            'to_direction',
            'transporter',
            'transporter_id',
            'direction_id',
        )

    def validate(self, data):
        if data['estimated_arrival_date'] < data['sent_date']:
            raise serializers.ValidationError(
                "Sent date cannot be greater than estimated date")
        return data


class ShipmentPatchSerializer(serializers.ModelSerializer):
    is_arrived = serializers.BooleanField(write_only=True)

    class Meta:
        model = Shipment
        fields = (
            'is_arrived',
        )
