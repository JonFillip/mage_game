import pygame
import sys

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


def keys():
    """Print the event attribute when user action detected."""
    pygame.init()
    pygame.display.set_mode(0, 0, 0)
    pygame.display.set_caption("Ready Player Zero")
    while True:
        # Watch for keyboard events.
        for event in pygame.event.get(events):
            if event.type in events:
                print(event.type)
            elif event.key == pygame.K_q:
                sys.exit()
