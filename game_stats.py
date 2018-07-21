class GameStats():
    """ Track game statistics."""

    def __init__(self, ai_settings):
        """ Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """ Statistics that change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1