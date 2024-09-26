import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


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

    # modify the player's position
    def move(self, dt):
        # 1. start with a unit vector pointing up from (0,0) to (0,1)
        # 2. Rotate that vector by the player's rotation so it points where the player is facing
        # 3. Multiply by PLAYER_SPEED * dt
        # 4. Add the vector to our position to move the player.

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        pass

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

            # call the move method
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
