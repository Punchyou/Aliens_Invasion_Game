class GameStats():
    """ Track game statistics."""

    def __init__(self, ai_settings):
        """ Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
    
    def reset_stats(self):
        """ Statistics that change during the game."""
        self.ships_left = self.ai_settings.ship_limit