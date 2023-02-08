from .particle import Particle
from . import BaseObject
from ..utils import Kilogram, vec2d
import pygame

DEFAULT_PARTICLE_COLOR = pygame.color.Color(255, 255, 255)

class SingleParticle(BaseObject):

    def __init__(self, pos: vec2d, color: pygame.color.Color=DEFAULT_PARTICLE_COLOR, mass: Kilogram=Kilogram(1)) -> None:

        self.image = pygame.surface.Surface((30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, color, self.rect.center, 5)
        self.rect.center = tuple(pos)
        super().__init__(self.rect, self.image)

        self.mainParticle = Particle(mass, pos)
    
    def update(self) -> None:
        from ..utils import ConfigLoader
        self.mainParticle.appliedForces.append(vec2d(0, 1) * ConfigLoader.gravityConstant * self.mainParticle.mass.value)
        self.mainParticle.tickMechanics()
        self.rect.center = self.mainParticle.pos
        
        from pygame import mouse

        if mouse.get_pressed()[0] and mouse.get_pos()[0] < 1280:
            self.mainParticle.move(vec2d(mouse.get_pos()), offset=False)
            self.mainParticle.velocity = vec2d(0, 0)
            self.mainParticle.accelerate = vec2d(0, 0)