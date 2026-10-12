import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)
