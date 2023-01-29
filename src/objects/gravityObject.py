from .baseObject import BaseObject
from ..utils.math import vec2d
from ..utils.unit import kilogram
import pygame

class GravityObject(BaseObject):

    def __init__(self, mass: kilogram, pos: vec2d, rect: pygame.Rect, img: pygame.Surface) -> None:
        super().__init__(mass, pos, rect, img)

    def update(self):
        # positive number moves downward
        force = vec2d(0, 1) * self.mass.getValue()
        self.appliedForce.append(force)
        super().update()