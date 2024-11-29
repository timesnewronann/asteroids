import pygame
import random
from pygame.math import Vector2
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity if velocity else Vector2(0, 0)

    def draw(self, screen):
        # pygame.draw.circle(surface, color, center, radius, width)
        pygame.draw.circle(screen, "white", (self.position.x,
                           self.position.y), self.radius, 2)

    def update(self, dt):
        # updates based only on its velocity and time delta
        self.position += self.velocity * dt

    def split(self):
        # always kill before any checks
        self.kill()
        # check the radius of the asteroid using self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            # return to end the method
            return

        # generate a random angle between 20-50 degrees
        random_angle = random.uniform(20, 50)

        # create two velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create the new asteroids within split because, we have all the information here, splitting is part of asteroids logic
       # create the new asteroids with current position
        Asteroid(self.position.x, self.position.y, new_radius, velocity1 * 1.2)
        Asteroid(self.position.x, self.position.y, new_radius, velocity2 * 1.2)
