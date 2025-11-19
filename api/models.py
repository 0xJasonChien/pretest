from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

from pretest.models import BaseModel

if TYPE_CHECKING:
    from .serializers import CreateOrderSerializer


class Order(BaseModel):
    order_number = models.BigAutoField(primary_key=True, verbose_name='訂單編號')
    total_price = models.PositiveIntegerField(verbose_name='訂單總價', default=0)

    @classmethod
    def create_order(
        cls: Order,
        serializer: CreateOrderSerializer,
    ) -> tuple[Order, list[ProductSnapshot]]:
        order = Order.objects.create()
        to_purchase_products_uuids = [
            item['uuid'] for item in serializer.validated_data['products']
        ]
        product_uuid_map = Product.get_product_uuid_map(to_purchase_products_uuids)

        product_snapshot_list = []
        total_price = 0
        for product_data in serializer.validated_data:
            product = product_uuid_map.get(str(product_data['uuid']))

            if not product:
                msg = 'Product does not exist'
                raise ValueError(msg)

            quantity = product_data['quantity']
            product_snapshot = product.create_snapshot(
                order=order,
                quantity=quantity,
            )
            total_price += product_snapshot.price * quantity
            product_snapshot_list.append(product_snapshot)

        order.total_price = total_price
        order.save()

        return order, product_snapshot_list


class Product(BaseModel):
    uuid = models.UUIDField(primary_key=True, verbose_name='商品 UUID')
    product_name = models.CharField(max_length=100, verbose_name='商品名稱')
    price = models.PositiveIntegerField(verbose_name='商品價格')

    @classmethod
    def get_product_uuid_map(
        cls: Product,
        to_filter_uuid: list[str],
    ) -> dict[str, Product]:
        return {
            str(product.uuid): product
            for product in Product.objects.filter(uuid__in=to_filter_uuid)
        }

    def create_snapshot(
        self: Product,
        order: Order,
        quantity: int,
    ) -> ProductSnapshot:
        return ProductSnapshot.objects.create(
            order=order,
            product=self,
            product_name=self.product_name,
            price=self.price,
            quantity=quantity,
        )


class ProductSnapshot(BaseModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='訂單',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        verbose_name='商品',
        null=True,
    )
    product_name = models.CharField(max_length=100, verbose_name='商品名稱')

    price = models.PositiveIntegerField(verbose_name='商品價格')
    quantity = models.PositiveIntegerField(verbose_name='商品數量')
