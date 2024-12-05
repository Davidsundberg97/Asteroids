from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.score = 0  # Initialize score attribute
        self.shot_radius = SHOT_RADIUS  # Initialize shot radius
        self.shield = 0  # Initialize shield duration
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        if self.shield > 0:
            pygame.draw.circle(screen, "blue", self.position, self.radius + 5, 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        self.timer -= dt
        if self.shield > 0:
            self.shield -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.rotate(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        if self.timer > 0:
            return
        else:
            shot = Shot(self.position.x, self.position.y, self.shot_radius)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot.score = self.score  # Link shot score to player score

    def handle_collision(self, asteroid):
        if self.shield > 0:
            self.shield = 0  # Remove shield
            asteroid.split()  # Split the asteroid
        else:
            print("Game Over!")
            return True  # Indicate game over
        return False  # Indicate game continues
