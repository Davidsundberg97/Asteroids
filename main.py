import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import PowerUp


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)
    PowerUp.containers = (powerups, updatable, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Display the player's score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        for obj in asteroids:
            if player.collision(obj):
                if player.handle_collision(obj):
                    return  # End game if player dies

        for obj in asteroids:
            for shot in shots_group:
                if shot.collision(obj):
                    obj.split()
                    shot.kill()
                    player.score += 10  # Increment score when an asteroid is destroyed
                    break

        for powerup in powerups:
            if player.collision(powerup):
                powerup.kill()
                if powerup.type == "shot":
                    player.shot_radius += 2  # Increase player's shot radius when power-up is collected
                elif powerup.type == "shield":
                    player.shield = SHIELD_DURATION  # Activate shield


if __name__ == "__main__":
    main()
