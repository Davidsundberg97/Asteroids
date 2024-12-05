from constants import *
from circleshape import CircleShape
import pygame

class Shot (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Use the passed radius
        self.score = 0  # Initialize score attribute
    
    def draw(self, screen):
        pygame.draw.circle(screen, "grey", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt



