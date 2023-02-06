from .particle import Particle
from . import BaseObject
from ..utils import vec2d
import pygame

class ParticleObject(BaseObject):

    def __init__(self, pos: vec2d) -> None:

        self.image = pygame.surface.Surface((30, 30))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (255, 255, 255), self.rect.center, 5)
        self.rect.center = tuple(pos)
        super().__init__(self.rect, self.image)
    