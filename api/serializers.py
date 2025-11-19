from rest_framework import serializers

from pretest.serializers import BaseSerializer


class ImportOrderSerializer(BaseSerializer):
    order_number = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        read_only_fields = (*BaseSerializer.Meta.read_only_fields, 'order_number')
