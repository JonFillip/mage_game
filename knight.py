import pygame


class Mage:
    """A class that manages the character mage"""

    def __init__(self, ap_game):
        """Initialize the mage and set its starting position."""
        self.neg = 0
        self.screen_window = ap_game.screen_window
        self.settings = ap_game.settings
        self.screen_window_rect = ap_game.screen_window.get_rect()

        # Load images for character walking movement
        self.walk_left = [
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/left_walk1.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/left_walk2.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/left_walk3.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/left_walk4.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/left_walk5.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/left_walk6.bmp")
        ]
        self.walk_right = [
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/walk1.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/walk2.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/walk3.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/walk4.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/walk5.bmp"),
            pygame.image.load("/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin"
                              "-mage-viking-free-pixel-art-game-heroes/Mage/Walk/walk6.bmp")
        ]

        # Load the character - mage mage and get its rect.
        image_file = "/Users/johnphillip/Desktop/alien_apocalypse/AlienApocalypse/craftpix-891165-assassin-mage" \
                     "-viking-free-pixel-art-game-heroes/Mage/Walk/standing.bmp"

        self.mage = pygame.image.load(image_file)
        self.rect = self.mage.get_rect()

        # Start each new character at the bottom center of the screen.
        self.rect.midbottom = self.screen_window_rect.midbottom

        # Store the decimal value for the mage's horizontal position.
        self.x = float(self.rect.x)
        # Store the decimal value for the `mage's vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.jump_move = False
        self.standing = True
        self.walk_count = 0
        self.jump_count = 10
        self.last_move = ""

    def update(self):
        """Update the mage's position based on the movement flag."""
        # Update the mage's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_window_rect.right:
            self.x += self.settings.knight_speed
            self.standing = False

        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.knight_speed
            self.standing = False

        else:
            self.standing = True
            self.walk_count = 0

        if self.jump_move:
            if self.jump_count >= -10:
                self.neg = 1
                if self.jump_count < 0:
                    self.neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * self.neg
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.jump_move = False

        # Update rect object from self.x.
        self.rect.x = self.x
        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the character at its current location."""
        if self.walk_count + 1 >= 18:
            self.walk_count = 0

        if not self.standing:
            if self.moving_left:
                self.screen_window.blit(self.walk_left[self.walk_count // 3], self.rect)
                self.walk_count += 1
                self.last_move = "left"

            elif self.moving_right:
                self.screen_window.blit(self.walk_right[self.walk_count // 3], self.rect)
                self.walk_count += 1
                self.last_move = "right"
        else:
            if self.last_move == "right":
                self.screen_window.blit(self.walk_right[0], self.rect)  # Set the blit to load last image facing right
            elif self.last_move == "left":
                self.screen_window.blit(self.walk_left[0], self.rect)  # Set the blit to load last image facing left
            else:
                self.screen_window.blit(self.mage, self.rect)
