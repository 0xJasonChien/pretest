from rest_framework import serializers


class BaseSerializer(serializers.Serializer):
    token = serializers.CharField()

    class Meta:
        read_only_fields = ('token',)
