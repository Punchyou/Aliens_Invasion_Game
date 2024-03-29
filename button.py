import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """
        Button to start the game.

        Parameters
        ----------
        ai_settings : 
            settings.Settings class
        screen :
            pygame.Surface
        msg :
            str. Message of the "Play" button. Can be just "Play"

        Returns
        -------
        None.

        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimentions of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Built button's rect objecr and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button messsage needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        Prepare the message of the game start button.

        Parameters
        ----------
        msg :
            str. Message of the "Play" button. Can be just "Play"

        Returns
        -------
        None.

        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Draw the start game button and its message.

        Returns
        -------
        None.

        """
        # Draw the button and the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)