from rest_framework import serializers

from .models import Product


class OrderDetailProductSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)


class OrderDetailSerializer(serializers.Serializer):
    product = OrderDetailProductSerializer()
    name = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField(read_only=True)


class OrderListSerializer(serializers.Serializer):
    order_number = serializers.IntegerField(read_only=True)
    total_price = serializers.IntegerField()
    product = OrderDetailSerializer(many=True, read_only=True)


class CreateOrderSerializer(serializers.Serializer):
    products = OrderDetailSerializer(many=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'price')
