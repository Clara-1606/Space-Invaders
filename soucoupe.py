import pygame
from pygame.sprite import Sprite
 
class Soucoupe(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/soucoupe.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = 550
        self.rect.y = 10

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)