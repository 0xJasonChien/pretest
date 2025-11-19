from rest_framework import serializers


class BaseSerializers(serializers.Serializer):
    token = serializers.CharField()

    class Meta:
        read_only_fields = ('token', 'order_number')
