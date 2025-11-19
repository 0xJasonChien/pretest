from django.db import models

from pretest.models import BaseModel


class Order(BaseModel):
    order_number = models.BigAutoField(primary_key=True)
    total_price = models.PositiveIntegerField(verbose_name='訂單總價')
