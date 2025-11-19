from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import ImportOrderSerializer

ACCEPTED_TOKEN = ('omni_pretest_token',)


@api_view(['POST'])
def import_order(request: HttpRequest) -> Response:
    serializer = ImportOrderSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.validated_data, status=201)

    data = serializer.validated_data

    if data['token'] not in ACCEPTED_TOKEN:
        return Response(
            {'detail': 'Invalid token'},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    order = Order.objects.create(
        amount=data['amount'],
    )

    return Response(
        ImportOrderSerializer(data=order).data,
    )
