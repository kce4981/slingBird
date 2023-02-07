from .interface import Mechanics
from .baseObject import BaseObject
from pygame.rect import Rect
from pygame.surface import Surface
from ..utils import Kilogram, ConfigLoader, ClockLoader, vec2d
from typing import Self


class GravityObject(BaseObject, Mechanics):


    def __init__(self, rect: Rect, background: Surface, mass: Kilogram) -> None:
        super().__init__(rect, background)
        self.initMechanics(mass)

    @classmethod
    def fromObject(cls, obj: BaseObject, mass: Kilogram) -> Self:
        return cls(obj.rect, obj.image, mass)

    # Overriding
    def update(self) -> None:
        gravityConstant = ConfigLoader.gravityConstant

        gravity = vec2d(0, 1) * gravityConstant * self.mass.getValue() * ClockLoader.getTime()
        self.appliedForces.append(gravity)

        self.tickMechanics()
        

        # this selection is for test purposes
        from pygame import mouse

        if mouse.get_pressed()[1]:
            print(self._accelerate, self.velocity)

        if mouse.get_pressed()[0]:
            offset = vec2d(*mouse.get_pos()) - vec2d(self.rect.center)
            self.move(offset)