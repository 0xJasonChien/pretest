from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='最後更新時間')

    class Meta:
        abstract = True


class Order(BaseModel):
    order_number = models.AutoField(unique=True, verbose_name='訂單編號')
    total_price = models.PositiveIntegerField(verbose_name='訂單總價')
