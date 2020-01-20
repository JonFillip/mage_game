import pygame
import sys
from pygame.locals import *

events = [
    pygame.KEYDOWN,
    pygame.KEYUP,
    pygame.MOUSEMOTION,
    pygame.MOUSEBUTTONDOWN,
    pygame.MOUSEBUTTONUP,
    pygame.JOYAXISMOTION,
    pygame.JOYBALLMOTION,
    pygame.JOYHATMOTION,
    pygame.JOYBUTTONDOWN,
    pygame.JOYBUTTONUP,
    pygame.VIDEORESIZE,
    pygame.VIDEOEXPOSE,
    pygame.QUIT,
    pygame.SYSWMEVENT,
    pygame.USEREVENT,
]


class Keys:
    """Print the event attribute when user action detected."""

    def __init__(self):
        """Initialize game screen."""
        pygame.init()

        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Ready Player Zero")
        self.clock = pygame.time.Clock()

    def run_window(self):
        """Start the loop for the game."""
        while True:
            # Watch for keyboard events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User quit game.")
                    sys.exit()
            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    """Make a game instance and run the game"""
    game = Keys()
    game.run_window()
