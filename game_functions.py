import sys
import pygame

def check_events(ship):
    '''Check keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    '''Update images on the screen'''
    #fill background with color
    screen.fill(ai_settings.bg_color)
    #draw the ship on the screen at a specific position
    ship.blitme()
    # Make the screen visible
    pygame.display.flip()
        