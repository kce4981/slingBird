from ..objects import SingleParticle, ParticleSquare
from . import BaseScene
from ..utils import vec2d
import pygame

class ParticleTest(BaseScene):

    def __init__(self):

        self.group = pygame.sprite.Group()

        #particle = SingleParticle(vec2d(30, 30))
        #particle.add(self.group)

        pSquare = ParticleSquare(vec2d(30, 30), 50)
        pSquare.add(self.group)


    def draw(self, surface: pygame.surface.Surface):
        self.group.update()
        self.group.draw(surface)