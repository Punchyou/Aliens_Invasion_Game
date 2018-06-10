import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' A class for a single alien ship in the fleet.'''
    def __init__(self, ai_settings, screen):
        '''Initialize the alien and its starting position.'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()

        # Start each new alien near to the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store tha alien's exact position.
        self.x = float(self.rect.x)
    
    def blitme(self):
        '''Draw the alien at it's current position.'''
        self.screen.blit(self.image, self.rect)