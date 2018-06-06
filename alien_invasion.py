import sys
import pygame
from settings import Settings

def run_game():
    # Initialize game and create a screen object
    # It's called surface
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)

    pygame.display.set_caption("Alien Invasion")

    # Set background color
    bg_color = (120, 50, 250)
    
    # Main loop of game
    while True:

        # Watch keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #fill cavkground with color
        screen.fill(ai_settings.bg_color)

        # Make the screen visible
        pygame.display.flip()
run_game()