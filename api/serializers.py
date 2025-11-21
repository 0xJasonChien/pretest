from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()


class ProductSnapshotSerializer(serializers.Serializer):
    product = ProductSerializer()
    name = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField()
    price = serializers.FloatField(read_only=True)


class OrderListSerializer(serializers.Serializer):
    order_number = serializers.IntegerField(read_only=True)
    total_price = serializers.IntegerField()
    product = ProductSnapshotSerializer(many=True, read_only=True)


class CreateOrderSerializer(serializers.Serializer):
    products = ProductSnapshotSerializer(many=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'price')
