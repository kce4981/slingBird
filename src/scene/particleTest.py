from ..objects import SingleParticle, ParticleSquare, Spring
from . import BaseScene
from ..utils import vec2d
import pygame

class ParticleTest(BaseScene):

    def __init__(self):

        super().__init__()

        #particle = SingleParticle(vec2d(30, 30))
        #particle.add(self.group)

        pSquare = ParticleSquare(vec2d(300, 300), 20)
        spring = Spring(vec2d(300, 200), pSquare.mainParticle, 1, length=50)

        self.addGroup(pSquare, spring)
