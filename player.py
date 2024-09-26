import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y):
        # Call the circle shape constructor
        # intialize the rotation
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # define the other methods
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    # override the parent draw method
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
