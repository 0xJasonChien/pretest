from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pretest.authenticate import token_required

from .serializers import OrderSerializer


@api_view(['POST'])
@token_required
def import_order(request: HttpRequest) -> Response:
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data, status=201)

    return Response(
        {'errors': serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )
