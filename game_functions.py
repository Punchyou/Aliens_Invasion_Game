import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    Respond to keypresses

    Parameters
    ----------
    event :
        Event class
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface object
    ship :
        ship.ship class
    bullets :
        settings.Settings

    Returns
    -------
    None.

    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Create a new bullet to add it in the bullets group

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame surfce object
    ship : 
        ship.Ship class
    bullets :
        pygame.sprite.Group class

    Returns
    -------
    None.

    """
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """
    Respond to keypresses

    Parameters
    ----------
    event :
        Event class
    ship :
        ship.Ship

    Returns
    -------
    None.

    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """
    Check keypresses and mouse events

    Parameters
    ----------
    ai_settings :
        settings.Settings object
    screen :
        pygame.surface class
    stats :
        game_stats.GameStat
    sb :
        scoreboard.Scoreboard object
    play_button :
        button.Button class
    ship :
        ship.Ship class
    aliens :
        pygame.sprite.Group class
    bullets :
        pygame.sprite.Group class

    Returns
    -------
    None.

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                ai_settings,
                screen,
                stats,
                sb,
                play_button,
                ship,
                aliens,
                bullets,
                mouse_x,
                mouse_y,
            )


def check_play_button(
    ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y
):
    """
    Start a new game when the player hits play.

    Parameters
    ----------
    ai_settings : 
        settings.Settings
    screen :
        pygame.surface object
    stats :
        game_stats.GameStats class
    sb :
        scoreboard.Scoreboard class
    play_button : 
        button.Button class
    ship :
        ship.Ship class
    aliens : 
        pygame.sprite.Group class
    bullets :
        pygame.sprite.Group class
    mouse_x :
        float
    mouse_y :
        float

    Returns
    -------
    None.

    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    # The play button needs to deactivate each time the game is active.
    if button_clicked and not stats.game_active:
        # Reset game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the cursor.
        pygame.mouse.set_visible(False)
        # Reset the game stats.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # Empty aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create new fleet.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """
    Update images on the screen

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface class
    stats :
        game_stats.GameStats class
    sb :
        scoreboard.Scoreboard class
    ship :
        ship.Ship class
    aliens :
        pygame.sprite.Group class
    bullets : 
        pygame.sprite.Group class
    play_button :
        button.Button class

    Returns
    -------
    None.

    """
    # fill background with color
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # draw the ship on the screen at a specific position
    ship.blitme()
    aliens.draw(screen)
    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the screen visible
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Update position of bullets and get rif of old bullets.

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface class
    stats :
        game_stats.GameStats class
    sb :
        scoreboard.Scoreboard
    ship :
        ship.Ship
    aliens :
        pygame.sprite.Group
    bullets :
        pygame.sprite.Group

    Returns
    -------
    None.

    """
    # Update bullets positions.
    bullets.update()

    # Get rid of bullets that have disappearred.
    for bullet in bullets.copy():
        # Don't remove items from a list or group within a for loop
        # Loop over a copy of the
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(
    ai_settings, screen, stats, sb, ship, aliens, bullets
):
    """
    Check the bullets that have hit the aliens and increse level and speed
    if there are no aliens left.

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface object
    stats :
        game_stats.GameStats class
    sb :
        scoreboard.Scoreboard
    ship :
        ship.Ship class
    aliens :
        pygame.sprite.Group class
    bullets :
        pygame.sprite.Group

    Returns
    -------
    None.

    """
    # Check for any bullets that have hit aliens, with groupcollide().
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # Destroy existing bullets, speed up game and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()
        sb.prep_ships()

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_alliens_x(ai_settings, alien_width):
    """
    Determine the number of aliens that fit in a row.

    Parameters
    ----------
    ai_settings :
        settings.Settings object
    alien_width :
        int

    Returns
    -------
    number_aliens_x :
        int

    """
    avaliable_spaxe_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_spaxe_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """
    Determine the number of rows of aliens that fit on the screen.

    Parameters
    ----------
    ai_settings :
        settings.Settings object
    ship_height :
        int
    alien_height :
        int

    Returns
    -------
    number_rows :
        int

    """
    availiable_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(availiable_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """
    Crete alien object and fix position.

    Parameters
    ----------
    ai_settings :
        settings.Settings
    screen :
        pygame.surface class
    aliens :
        pygame.sprite.Group
    alien_number :
        int
    row_number :
        int

    Returns
    -------
    None.

    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    Create a full fleet of aliens.

    Parameters
    ----------
    ai_settings :
        settings.Settings object
    screen :
        pygame.surface
    ship :
        ship.Ship
    aliens :
        pygame.sprite.Group
    Returns
    -------
    None.

    """
    # Create an alien and find the nuber of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create fleet of aliens.
    for row_number in range(number_rows):
        # Create row of aliens.
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """
    Check if any alien has reached an edge.

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    aliens : 
        pygame.sprite.Group

    Returns
    -------
    None.

    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """
    Drop entire fleet and change its direction.

    Parameters
    ----------
    ai_settings : 
        settings.Settings class
    aliens :
        pygame.sprite.Group

    Returns
    -------
    None.

    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Respond to ship being hit by an alien, by losing a life.

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface object
    stats :
        game_stats.GameStats class
    sb :
        scoreboard.Scoreboard class
    ship :
        ship.Ship class
    aliens :
        pygame.sprite.Group class
    bullets :
        pygame.sprite.Group class

    Returns
    -------
    None.

    """
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create new fleet.
        create_fleet(ai_settings, screen, ship, aliens)

        # Center the ship.
        ship.center_ship()

        # Pause for a while.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Check if any aliens have reached the bottom of the screen.

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface object
    stats :
        game_stats.GameStats
    sb :
        coreboard.Scoreboard
    ship :
        ship.Ship
    aliens :
        pygame.sprite.Group
    bullets :
        pygame.sprite.Group

    Returns
    -------
    None.

    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Same as ship_hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Update the position of all aliens in the fleet.
    Check if the fleet is at the edge.

    Parameters
    ----------
    ai_settings :
        settings.Settings class
    screen :
        pygame.surface object
    stats :
        game_stats.GameStats
    sb :
        scoreboard.Scoreboard
    ship :
        ship.Ship
    aliens :
        pygame.sprite.Group
    bullets :
        pygame.sprite.Group

    Returns
    -------
    None.

    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    """
    Check if there's a new high score.

    Parameters
    ----------
    stats :
        game_stats.GameStats class
    sb :
        scoreboard.Scoreboard class

    Returns
    -------
    None.

    """
    if stats.score > stats.score:
        stats.high_score = stats.score
        sb.prep_high_score()
