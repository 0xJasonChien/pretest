from collections.abc import Callable
from functools import wraps

from rest_framework import status
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from .config import settings


def token_required(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(request: HttpRequest, *args: tuple, **kwargs: dict) -> Response:
        auth_header = request.headers.get('Authorization')
        token = auth_header.split(' ')[1] if auth_header else None

        if not token or token not in settings.ACCEPTED_TOKEN:
            return Response(
                {'detail': 'Invalid token'},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return func(request, *args, **kwargs)

    return wrapper
