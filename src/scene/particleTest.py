from ..objects import SingleParticle, ParticleSquare, Spring
from . import BaseScene
from ..utils import vec2d
import pygame

class ParticleTest(BaseScene):

    def __init__(self):

        self.group = pygame.sprite.Group()

        #particle = SingleParticle(vec2d(30, 30))
        #particle.add(self.group)

        pSquare = ParticleSquare(vec2d(300, 100), 20)
        pSquare.add(self.group)

        mainParticle = pSquare.group.particle[0]

        spring = Spring(vec2d(300, 15), mainParticle, .1, length=50)
        spring.add(self.group)


    def draw(self, surface: pygame.surface.Surface):
        self.group.update()
        self.group.draw(surface)