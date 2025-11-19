from django.db import models

from pretest.models import BaseModel


class Order(BaseModel):
    order_number = models.BigAutoField(primary_key=True, verbose_name='訂單編號')
    total_price = models.PositiveIntegerField(verbose_name='訂單總價')


class Product(BaseModel):
    product_name = models.CharField(max_length=100, verbose_name='商品名稱')
    price = models.PositiveIntegerField(verbose_name='商品價格')


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
