from __future__ import annotations

from typing import TYPE_CHECKING, Any

from rest_framework.response import Response
from rest_framework.views import exception_handler

if TYPE_CHECKING:

    from rest_framework.exceptions import APIException


def custom_exception_handler(
    exc: APIException | Exception,
    context: dict[str, Any],
) -> Response:
    response = exception_handler(exc, context)

    if response and isinstance(response.data, dict):
        response.data = {
            'detail': response.data,
            'success': False,
        }
        return response

    return Response(
        {'detail': str(exc), 'success': False},
        status=500,
    )
