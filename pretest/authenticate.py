from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from .config import settings

ACCEPTED_TOKEN = settings.ACCEPTED_TOKEN

def token_required(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        token = request.data.get('token')
        if token not in ACCEPTED_TOKEN:
            return Response(
                {'detail': 'Invalid token'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return func(request, *args, **kwargs)
    return wrapper