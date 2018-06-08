import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    '''Initialize game and create a screen object'''
    '''It's called surface'''
    pygame.init()

    # Set the screen settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)
    
    # Main loop of game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
run_game()