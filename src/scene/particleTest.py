from ..objects import ParticleObject
from . import BaseScene
from ..utils import vec2d
import pygame

class ParticleTest(BaseScene):

    def __init__(self):

        self.group = pygame.sprite.Group()

        particle = ParticleObject(vec2d(30, 30))
        particle.add(self.group)


    def draw(self, surface: pygame.surface.Surface):
        self.group.update()
        self.group.draw(surface)