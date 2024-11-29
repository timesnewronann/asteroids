# Shot should inherit from CircleShape (like Asteroid)

# import CircleShape from circleShape.py
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


# Create shot class


class Shot(CircleShape):
    # constructor
    def __init__(self, position):
        # Call parent class's __init__ witht the position and radius
        super().__init__(position.x, position.y, SHOT_RADIUS)
        # Initialize any shot-specific attributes
        self.velocity = pygame.math.Vector2()

    def update(self, dt):
        # Update shot position based on velocity and time
        # Takes our current position -> adds velcoity * dt = bullets move in whatever direction our velocity is set to
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw screen
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
