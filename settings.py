class Settings():
    # A class that includes all settings for Aliens Invasion

    def __init__(self):
        """Initialize game's static settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (120, 50, 250)

        # Ship's settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 98, 253, 98

        # Drop speed for how quickly the fleet drops down the screen.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase.
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.4

        #Scoring.
        self.alien_points = 50

        # 1 = right, -1 = left
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increasing speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)