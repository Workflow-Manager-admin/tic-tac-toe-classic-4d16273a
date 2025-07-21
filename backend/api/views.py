from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# PUBLIC_INTERFACE
@swagger_auto_schema(
    method='get',
    operation_summary="Health Check",
    operation_description="Returns server health status. Use this to verify that the backend service is up.",
    responses={200: openapi.Response(description="Success", examples={"application/json": {"message": "Server is up!"}})},
    tags=['health']
)
@api_view(['GET'])
def health(request):
    """Health check endpoint.
    Returns:
        200 OK: {"message": "Server is up!"}
    """
    return Response({"message": "Server is up!"}, status=status.HTTP_200_OK)

# PUBLIC_INTERFACE
@swagger_auto_schema(
    method='get',
    operation_summary="Stub: List Game Histories",
    operation_description="Stub endpoint for listing stored past games. No real data for now. Intended for future extensibility.",
    responses={200: openapi.Response(description="Success", examples={"application/json": {"games": []}})},
    tags=['game-history']
)
@api_view(['GET'])
def game_history_stub(request):
    """Stub endpoint for listing stored past games (for extensibility).

    Currently returns an empty list. Intended for future implementation of history storage.

    Returns:
        200 OK: {"games": []}
    """
    return Response({"games": []}, status=status.HTTP_200_OK)
