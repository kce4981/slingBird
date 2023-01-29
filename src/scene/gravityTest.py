from .baseScene import BaseScene
from ..objects import GravityObject
from .. utils import unit
import pygame


class GravityTest(BaseScene):

    def __init__(self):

        mass = unit.kilogram(3)
        img = pygame.Surface((30, 30))
        img.fill(pygame.Color(119, 41, 241))
        rect = img.get_rect()

        obj = GravityObject(mass, (0, 0), rect, img)
        self.newGroup = pygame.sprite.Group()
        obj.add(self.newGroup)


    def draw(self, surface: pygame.Surface):
        self.newGroup.update()
        self.newGroup.draw(surface)
