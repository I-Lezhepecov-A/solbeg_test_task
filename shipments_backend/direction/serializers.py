from rest_framework import serializers

from .models import Direction


class DirectionDetailSerializer(serializers.ModelSerializer):
    country = serializers.CharField()
    city = serializers.CharField()

    class Meta:
        model = Direction
        fields = (
            'country',
            'city'
        )


class DirectionSerializer(DirectionDetailSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Direction
        fields = (
            'id',
            'country',
            'city'
        )
