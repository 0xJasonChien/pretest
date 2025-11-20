from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pretest.authentication import token_required

from .models import Order, Product
from .serializers import CreateOrderSerializer, OrderListSerializer, ProductSerializer


@api_view(['POST'])
@token_required
def import_order(request: HttpRequest) -> Response:
    serializer = CreateOrderSerializer(data=request.data)

    if serializer.is_valid():
        created_order, product_snapshot_list = Order.create_order(serializer)

        response_data = {
            'order_number': created_order.order_number,
            'total_price': created_order.total_price,
            'product': product_snapshot_list,
        }
        created_data = OrderListSerializer(response_data)

        return Response(created_data.data, status=status.HTTP_201_CREATED)

    return Response(
        {'detail': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(['POST'])
@token_required
def import_product(request: HttpRequest) -> Response:
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        product = serializer.save()
        response_data = ProductSerializer(product)

        return Response(response_data.data, status=status.HTTP_201_CREATED)

    return Response(
        {'detail': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(['GET'])
@token_required
def list_product(request: HttpRequest) -> Response:  # noqa: ARG001
    queryset = Product.objects.all()
    response_data = ProductSerializer(queryset, many=True)

    return Response(response_data.data, status=status.HTTP_200_OK)
