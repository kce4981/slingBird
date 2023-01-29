from .baseObject import BaseObject
from ..utils.math import vec2d
from ..utils.unit import kilogram
import pygame

class GravityObject(BaseObject):

    def __init__(self, mass: kilogram, rect: pygame.rect.Rect, img: pygame.surface.Surface, screenRect=None) -> None:
        super().__init__(mass, rect, img, screenRect)

    def update(self):
        # positive number moves downward
        force = vec2d(0, 1) * self.mass.getValue()
        self.appliedForce.append(force)
        super().update()