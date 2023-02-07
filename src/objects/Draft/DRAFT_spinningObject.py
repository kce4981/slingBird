from ..interface import Mechanics
from .. import BaseObject
from pygame.rect import Rect
from pygame.surface import Surface
import pygame
from ...utils import Kilogram, vec2d
from typing import Self
import math


class SpinningObject(BaseObject, Mechanics):

    def __init__(self, rect: Rect, background: Surface, mass: Kilogram) -> None:
        super().__init__(rect, background)
        self.initMechanics(mass)

        self.theta = 0 # radian
        self.radius = 5

        self.velocity = vec2d(0, -10)

    @classmethod    
    def fromObject(cls, obj: BaseObject, mass: Kilogram) -> Self:
        return cls(obj.rect, obj.image, mass)


    def update(self) -> None:
        self._accelerate = self.velocity.rotate(90)
        self._accelerate /= 10
        print(self._accelerate, self.velocity)

        
        #elf.theta += math.radians(1)
        #self.accelerate = self.radius * vec2d(math.cos(self.theta), math.sin(self.theta))
        #self.velocity = self.radius * vec2d(math.sin(self.theta), math.cos(self.theta))
        #self.image = pygame.transform.rotate(self.image, 30)
        displacement = self.tickMechanics()
        # print(displacement)
        self.rect.move_ip(displacement)

