# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from pygame.locals import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # create two groups before the game loop
    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    # Create asteroid group
    asteroids = pygame.sprite.Group()

    # create container for asteroid to automatically add new instance
    Asteroid.containers = (asteroids, updatable, drawable)
    # Asteroid object will automaticalyl be a part of the asteroids group

    # Container for AsteroidField Instances
    AsteroidField.containers = (updatable,)

    # intialize asteroid field
    asteroidField = AsteroidField()

    # Create shots groups
    shots = pygame.sprite.Group()

    # Add the shots to the contianers
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    # instantiate a player object, pass these values to the constructor to spawn it in the middle of the screen
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        time_elapsed = clock.tick(60)

        dt = time_elapsed / 1000

        for update_object in updatable:
            update_object.update(dt)

        # perform collision check after updating the objects
        for asteroid in asteroids:
            if player.collisionCheck(asteroid):
                print("Game over!")
                sys.exit()

        # second collision check to check if shots hit the asteroids
        for asteroid in asteroids:
            for shot in shots:
                # check if the shot hit the asteroid
                if shot.collisionCheck(asteroid):
                    shot.kill()
                    asteroid.split()

                # re-render the player on the screen each frame
                # use player.draw(screen)
        for draw_object in drawable:
            draw_object.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
