from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            r = random.uniform(20,50)
            n_v1 = self.velocity.rotate(r)
            n_v2 = self.velocity.rotate(-r)
            self.radius -= ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, self.radius)
            a2 = Asteroid(self.position.x, self.position.y, self.radius)
            a1.velocity = n_v1*1.2 
            a2.velocity = n_v2*1.2