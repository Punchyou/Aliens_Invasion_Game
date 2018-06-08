import pygame

class Ship():

    def __init__(self, screen):
        # Initialize the ship and set its starting position

        self.screen = screen

        # Load the ship image
        self.image = pygame.image.load("images/spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 130))
        # Prepare a rectangular area for the image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set as starting position the center at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        # Dreaw the ship and the location
        self.screen.blit(self.image, self.rect)