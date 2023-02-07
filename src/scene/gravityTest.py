from . import BaseScene
from ..objects import BaseObject, GravityObject, SpinningObject, Spring
from ..utils import Kilogram, Face
from pygame.surface import Surface
from pygame import sprite
import pygame

class GravityTest(BaseScene):

    def __init__(self):

        self.group = sprite.Group()

        background = Surface((30, 30))
        background.fill((121, 204, 43))
        baseObject = BaseObject(background.get_rect().move(300, 300), background)

        mass = Kilogram(3)
        testGravity = GravityObject.fromObject(baseObject, mass)
        testGravity.add(self.group)

        testSpin = SpinningObject.fromObject(baseObject, mass)
        #testSpin.add(self.group)

        springBackground = Surface((10, 80))
        springBackground.fill((170, 170, 170))
        springBaseObj = BaseObject(springBackground.get_rect().move(310, 220), springBackground)

        testSpring = Spring.fromObject(springBaseObj, 1)
        testSpring.connect(testGravity, Face.DOWN)
        testSpring.add(self.group)



    def draw(self, surface: Surface):
        self.group.update()
        self.group.draw(surface)