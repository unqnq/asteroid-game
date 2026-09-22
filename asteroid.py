import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt:float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            aster1_vector = self.velocity.rotate(angle)
            aster2_vector = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            aster1 = Asteroid(self.position.x, self.position.y, new_radius)
            aster2 = Asteroid(self.position.x, self.position.y, new_radius)
            aster1.velocity = aster1_vector * 1.2
            aster2.velocity = aster2_vector * 1.2
