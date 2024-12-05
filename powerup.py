from circleshape import CircleShape
import pygame

class PowerUp(CircleShape):
    def __init__(self, x, y, powerup_type):
        super().__init__(x, y, 10)  # Power-up radius is 10
        self.type = powerup_type
    
    def draw(self, screen):
        color = "green" if self.type == "shot" else "blue"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    
    def update(self, dt):
        pass  # Power-ups do not move