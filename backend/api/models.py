from django.db import models

# Stub for future extension: game history storage

class GameHistory(models.Model):
    """
    Model stub for storing past Tic Tac Toe games (for future extensibility).

    Fields like moves, players, result, timestamp, etc. can be added as needed.
    """
    # Example stub fields for extensibility
    # winner = models.CharField(max_length=32, null=True, blank=True)
    # board_state = models.TextField()  # Could be a JSON/text tabular representation
    # played_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Game History"
        verbose_name_plural = "Game Histories"

# No active models required at present.
