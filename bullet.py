import pygame
from pygame.sprite import Sprite
from AlienApocalypse.knight import Mage


class Bullet(Sprite):
    """A class to manage bullets or sword throws fired by the mage or soldier."""

    def __init__(self, ap_game):
        """Create a bullet object at the mage's current position."""
        super().__init__()

        # Initialize the mage attributes and instances in bullet class
        self.mage = Mage(self)
        self.last_move = None

        self.bullet_image_right = [
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Fire_Extra/fire_right1.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Fire_Extra/fire_right2.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_right3.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_right4.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_right5.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire6.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire7.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire8.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire9.png")
        ]
        self.bullet_image_left = [
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_left1.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_left2.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_left3.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_left4.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire_left5.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire6.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire7.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire8.png"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/craftpix-891165-assassin-mage-viking-free"
                              "-pixel-art-game-heroes/Mage/Fire_Extra/fire9.png")
        ]
        self.screen = ap_game.screen_window
        self.settings = ap_game.settings
        self.color = ap_game.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height, self.rect)

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet forward of the players current facing direction."""
        self.x -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        if self.last_move == self.mage.moving_right:
            for bullet in self.bullet_image_right:
                self.screen.blit(self.screen, self.bullet_image_right, self.rect, bullet[1], 0, 0)
        elif self.last_move == self.mage.moving_left:
            for bullet in self.bullet_image_left:
                self.screen.blit(self.screen, self.bullet_image_left, self.rect, bullet[1], 0, 0)
