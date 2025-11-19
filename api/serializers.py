from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    token = serializers.CharField()

    class Meta:
        read_only_fields = ('token',)


class ImportOrderSerializer(BaseSerializer):
    order_number = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        read_only_fields = (*BaseSerializer.Meta.read_only_fields, 'order_number')
