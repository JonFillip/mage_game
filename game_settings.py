class GameSettings:
    """This class stores all the game settings"""

    def __init__(self):
        """Initialize the game's settings attributes"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0, 0, 255)

        # Knight settings
        self.knight_speed = 1.5
