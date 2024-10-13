import pygame

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisionCheck(self, new_circle):
        distance = self.position.distance_to(new_circle.position)

        #calculate the sum of self's radius and new_circle radius 
        sum_radii = self.radius + new_circle.radius

        if distance <= sum_radii:
            return True
        
        else: 
            return False 