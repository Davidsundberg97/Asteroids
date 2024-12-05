from circleshape import CircleShape
from constants import *
import pygame
import random
from powerup import PowerUp  # Import PowerUp class

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

        # Chance to drop a power-up
        if random.random() < POWER_UP_DROP_CHANCE:
            powerup_type = "shield" if random.random() < 0.5 else "shot"
            PowerUp(self.position.x, self.position.y, powerup_type)  # Pass powerup_type argument