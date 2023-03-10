from .particle import Particle
from . import BaseObject
from ..utils import vec2d
from typing import Optional
import pygame

class Spring(BaseObject):

    def __init__(self, pos: vec2d, particle: Particle, springConstant: float,  length: Optional[float]=None) -> None:

        self.pos = pos
        self.particle = particle
        self.springConstant = springConstant

        if length is None:
            self.initLength = self.getLengthVec2d()
        else:
            self.initLength = self.getLengthVec2d().normalize() * length

        self.image = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        pygame.draw.line(self.image, (80, 80, 80), pos, particle.pos, 5)
        super().__init__(self.rect, self.image)


    def update(self) -> None:
        from ..utils import ClockLoader

        length = self.getLengthVec2d()

        pygame.draw.line(self.image, (80, 80, 80), self.pos, self.particle.pos, 5)
        # self.rect.midtop = tuple(self.pos)
        springForce = (length - self.initLength) * -1 * self.springConstant 
        self.particle.appliedForces.append(springForce)


    def getLengthVec2d(self) -> vec2d:
        return self.particle.pos - self.pos
