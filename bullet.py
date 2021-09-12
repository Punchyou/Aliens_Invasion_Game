import pygame
# In order to group related elements in the game:
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    A class about the bullets that the ship fires.
    """
    def __init__(self, ai_settings, screen, ship):
        """
        Set bullet's object position at the ship's position.

        Parameters
        ----------
        ai_settings :
            settings.Settings class
        screen :
            pygame.Surface class
        ship :
            ship.Ship class

        Returns
        -------
        None.

        """

        # The super function can be used to gain access to inherited methods
        # from a parent or sibling class
        # that has been overwritten in a class object.
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a rect at (0, 0), 
        # because it's not based in an image, 
        # and then correct its position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top + 40

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """
        Move the bullet up the screen.

        Returns
        -------
        None.

        """
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """
        Draw the bullet to the screen.

        Returns
        -------
        None.

        """
        pygame.draw.rect(self.screen, self.color, self.rect)