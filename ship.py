import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''Initialize the ship and set its starting position.'''

        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image
        self.image = pygame.image.load("images/spaceship.png")
        self.image = pygame.transform.scale(self.image, (70, 90))
        # Prepare a rectangular area for the image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set as starting position the center at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        # Because rect will store only integers
        self.center = float(self.rect.centerx)


        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position."""

        # Update the ship's center value, not the rect
        # If keypress is right and the position is smaller than the right edge of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # The left edga starts at 0
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self,center
        self.rect.centerx = self.center
    
    def blitme(self):
        # Dreaw the ship and the location
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """ Center the ship."""
        self.center = self.screen_rect.centerx