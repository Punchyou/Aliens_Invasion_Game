class Settings():
    # A class that includes all settings for Aliens Invasion

    def __init__(self):
        """Initialize game's settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (120, 50, 250)

        # Ship's settings
        # Adjust the speed of the ship (by pixels)
        self.ship_speed_factor = 1

        # Bullet's settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 98, 253, 98

        # Alien's settings.
        self.alien_speed_factor = 0.4
        # Drop speed for how quickly the fleet drops down the screen.
        self.fleet_drop_speed = 3
        # Fleet direction of 1 is right, and -1 is left.
        self.fleet_direction = 1
