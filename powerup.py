
from circleshape import CircleShape
import pygame

class PowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 10)  # Power-up radius is 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)
    
    def update(self, dt):
        pass  # Power-ups do not move