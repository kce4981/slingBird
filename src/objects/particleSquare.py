from .particle import Particle, ParticleGroup
from . import BaseObject
from ..utils import Kilogram, vec2d
import pygame


class ParticleSquare(BaseObject):

    def __init__(self, topLeft: vec2d, radius: int) -> None:

        self.image = pygame.surface.Surface((radius, radius))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255, 255, 255), self.rect, radius)
        self.rect.topleft = tuple(topLeft)
        super().__init__(self.rect, self.image)

        self.group = ParticleGroup
        self.mainParticle = Particle(Kilogram(.25), vec2d(self.rect.topleft))
        ps = []
        ps.append(self.mainParticle)        
        ps.append(Particle(Kilogram(.25), vec2d(self.rect.topright)))
        ps.append(Particle(Kilogram(.25), vec2d(self.rect.bottomleft)))
        ps.append(Particle(Kilogram(.25), vec2d(self.rect.bottomright)))
        self.group(tuple(ps))
    
    def update(self) -> None:
        self.mainParticle.appliedForces.append(vec2d(0, 1) * .98)
        self.mainParticle.tickMechanics()
        self.rect.topleft = self.mainParticle.pos
        
        from pygame import mouse

        if mouse.get_pressed()[0]:
            self.mainParticle.move(vec2d(mouse.get_pos()), offset=False)
            self.mainParticle.velocity = vec2d(0, 0)
            self.mainParticle.accelerate = vec2d(0, 0)