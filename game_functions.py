import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' Respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Create a new bullet to add it in the bullets group'''
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''Respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''Check keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''Update images on the screen'''
    #fill background with color
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #draw the ship on the screen at a specific position
    ship.blitme()
    aliens.draw(screen)
    
    # Make the screen visible
    pygame.display.flip()

def update_bullets(bullets):
    ''' Update position of bullets and get rif of old bullets.'''
    # Update bullets positions.
    bullets.update()

    # Get rid of bullets that have disappearred.
    for bullet in bullets.copy():
    # Don't remove items from a list or group within a for loop
    # Loop over a copy of the 
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 

def create_fleet(ai_settings, screen, aliens):
    '''Create a full fleet of aliens.'''
    # Create an alien and find the nuber of aliens in a row.
    # Spacing between each alien is equal to one alien width.

    
    # This alien won't be part of the fleet.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    avaliable_spaxe_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_spaxe_x / (2 * alien_width))

    # First row of aliens.
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row.
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    " Check if any alien has reached an edge."
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    " Drop entire fleet and change its direction."
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """Update the position of all aliens in the fleet."""
    """Check if the fleet is at the edge."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()