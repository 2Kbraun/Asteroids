import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, cooldown=0):
        #self.x = x
        #self.y = y
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.cooldown = cooldown

        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        print("Triangle called")

        return [a, b, c]

    def draw(self, screen):
        print("draw called")
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.cooldown -= dt
    
    def move(self, dt: float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.cooldown > 0:
            pass
        else:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation))
            
            shot.velocity = (shot.velocity * PLAYER_SHOOT_SPEED)
            self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

         
