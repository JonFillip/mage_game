import sys
import os
import pygame
from game_settings import GameSettings
from knight import Mage
from bullet import Bullet


class AlienApocalypse:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = GameSettings()
        # Set up a clock that regulates the FPS of the game window
        self.clock = pygame.time.Clock()
        self.settings.vertical_momentum = 0

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

        self.screen_window = pygame.display.set_mode((self.settings.screen_width,
                                                      self.settings.screen_height))
        pygame.display.set_caption("Alien Apocalypse")

        """Setting background color"""
        self.background_color = (0, 0, 255)

        # Initialize the attributes for the Mage class
        self.mage = Mage(self)
        self.walking_step = 6
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self.clock.tick(27)
            self._check_events()
            self.mage.update()
            self._update_bullets()
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
            elif event.type == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keydown_event(self, event):
        """Respond to KEYDOWN presses"""
        if event.key == pygame.K_RIGHT:
            self.mage.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.mage.moving_left = True
        elif event.key == pygame.K_UP:
            self.mage.jump_move = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        """Respond to KEY releases"""
        if event.key == pygame.K_RIGHT:
            self.mage.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.mage.moving_left = False

    def _fire_bullet(self):
        """Create a bullet and add it to the group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of the old bullets and get rid of it."""
        # update the bullet position
        self.bullets.update()
        # To delete bullets that have been fired and disappeared from the screen
        for bullet in self.bullets.copy():
            if bullet.rect.x <= 1:
                self.bullets.remove(bullet)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen_window.fill(self.settings.background_color)
        self.mage.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        self.clock.tick(60)


if __name__ == "__main__":
    """Make a game instance, and run the game"""
    ap = AlienApocalypse()
    ap.run_game()
