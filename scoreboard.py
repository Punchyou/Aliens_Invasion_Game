import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """
    A class to represent the score.
    """

    def __init__(self, ai_settings, screen, stats):
        """
        Initialize scorekeeping attributes.

        Parameters
        ----------
        ai_settings :
            settings.Settings object
        screen :
            pygame.surface class
        stats :
            game_stats.GameStats

        Returns
        -------
        None.

        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """
        Turn the score into an image.

        Returns
        -------
        None.

        """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color
        )

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        Draw score to the screen.

        Returns
        -------
        None.

        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn high score into an image.

        Returns
        -------
        None.

        """
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color
        )

        # Center the high score.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """
        Turn the level into an image.

        Returns
        -------
        None.

        """
        self.level_image = self.font.render(
            str(self.stats.level), True, self.text_color,
            self.ai_settings.bg_color
        )

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.level_rect.top + 70

    def prep_ships(self):
        """
        Show how many live are left.

        Returns
        -------
        None.

        """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
