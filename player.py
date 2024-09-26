import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


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

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotate the triangle left and right
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # move forward and backward
        if keys[pygame.K_w]:
            # 1. Calculate the direction vector based on the current rotation
            # 2. Scale this vector by speed and dt
            # 3. Add this to the current position
            pass
