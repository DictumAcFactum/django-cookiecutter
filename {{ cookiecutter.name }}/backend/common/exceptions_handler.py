from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.serializers import as_serializer_error
from rest_framework.response import Response


def custom_exception_handler(exc, ctx):
    """
    {
        "message": "Error message",
        "extra": {}
    }
    """
    response = exception_handler(exc, ctx)

    if response is None:
        data = {
            "message": exc.message,
            "extra": exc.extra,
            }
        return Response(data, status=400)

    return response

