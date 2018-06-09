class Settings():
    # A class that includes all settings for Aliens Invasion

    def __init__(self):
        ''' Initialize game's settings'''
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (120, 50, 250)

        # Ship's settings
        # Adjust the speed of the ship (by pixels)
        self.ship_speed_factor = 1.2

        # Bullet's settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 98, 253, 98