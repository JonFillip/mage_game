import pygame


class Knight:
    """A class that manages the character knight"""

    def __init__(self, ap_game):
        """Initialize the knight and set its starting position."""
        self.screen_window = ap_game.screen_window
        self.settings = ap_game.settings
        self.screen_window_rect = ap_game.screen_window.get_rect()

        # Load the character - Knight image and get its rect.
        image_file = "/Users/johnphillip/Desktop/alien_apocalypse/craftpix" \
                     "-891165-assassin-mage-viking-free-pixel-art-game-heroes" \
                     "/knight.bmp"
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_window_rect.center

        # Store the decimal value for the knight's horizontal position.
        self.x = float(self.rect.x)
        # Store the decimal value for the `knight's vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the knight's position based on the movement flag."""
        # Update the knight's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_window_rect.right:
            self.x += self.settings.knight_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.knight_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.knight_speed

        if self.moving_down and self.rect.bottom < self.screen_window_rect.bottom:
            self.y += self.settings.knight_speed

        # Update rect object from self.x.
        self.rect.x = self.x
        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the character at its current location."""
        self.screen_window.blit(self.image, self.rect)
