class GameSettings:
    """This class stores all the game settings"""

    def __init__(self):
        """Initialize the game's settings attributes"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 255)
        self.vertical_momentum = 0

        # Knight settings
        self.knight_speed = 2.5

        # Bullet/Sword settings
        self.bullet_speed = 8.0
        self.bullet_color = (255, 60, 60)
        # self.facing = facing
        self.bullets_allowed = 1
