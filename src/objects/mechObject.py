from .interface import Mechanics
from . import BaseObject
from ..utils import Kilogram
import pygame

class MechObject(BaseObject, Mechanics):

    def __init__(self, rect: pygame.rect.Rect, background: pygame.surface.Surface, mass: Kilogram) -> None:
        super().__init__(rect, background)
        self.initMechanics(mass)