from .particle import Particle
from . import BaseObject
from ..utils import Kilogram, vec2d
import pygame

class SingleParticle(BaseObject):

    def __init__(self, pos: vec2d) -> None:

        self.image = pygame.surface.Surface((30, 30))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (255, 255, 255), self.rect.center, 5)
        self.rect.center = tuple(pos)
        super().__init__(self.rect, self.image)

        self.particle = Particle(Kilogram(1), pos)
    
    def update(self) -> None:
        self.particle.appliedForces.append(vec2d(0, 1) * .98)
        self.particle.tickMechanics()
        self.rect.center = self.particle.pos
        
        from pygame import mouse

        if mouse.get_pressed()[0]:
            self.particle.move(vec2d(mouse.get_pos()), offset=False)
            self.particle.velocity = vec2d(0, 0)
            self.particle.accelerate = vec2d(0, 0)