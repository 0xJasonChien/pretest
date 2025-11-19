from rest_framework import serializers


class ImportOrderSerializer(serializers.Serializer):
    token = serializers.CharField()
    order_number = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        read_only_fields = ('token', 'order_number')
