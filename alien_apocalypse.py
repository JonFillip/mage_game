import sys
import os
import pygame
from game_settings import GameSettings
from knight import Knight


class AlienApocalypse:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = GameSettings()

        drivers = ['directfb', 'fbcon', 'svgalib']

        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print('Driver: {0} failed.'.format(driver))
                continue
            found = True
            break

        if not found:
            raise Exception('No suitable video driver found!')

        self.screen_window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Apocalypse")

        """Setting background color"""
        self.background_color = (0, 0, 255)

        self.knight = Knight(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.knight.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Respond to KEYDOWN presses"""
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.knight.moving_left = True
        elif event.key == pygame.K_UP:
            self.knight.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.knight.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        """Respond to KEY releases"""
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.knight.moving_left = False
        elif event.key == pygame.K_UP:
            self.knight.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.knight.moving_down = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen_window.fill(self.settings.background_color)
        self.knight.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game"""
    ap = AlienApocalypse()
    ap.run_game()
