from django.urls import path
from .views import health, game_history_stub

urlpatterns = [
    path('health/', health, name='Health'),
    path('game-history/', game_history_stub, name='GameHistoryStub'),
]
