import sys
import pygame

def check_events():
    '''Check keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    '''Update images on the screen'''
    #fill background with color
    screen.fill(ai_settings.bg_color)
    #draw the ship on the screen at a specific position
    ship.blitme()
    # Make the screen visible
    pygame.display.flip()
        