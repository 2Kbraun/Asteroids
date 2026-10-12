import random

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity = v1 * 1.2
        new_asteroid2.velocity = v2 * 1.2
