from .interface import Mechanics
from . import BaseObject
from ..utils import Kilogram, vec2d
import pygame

class Spring(BaseObject, Mechanics):

    def __init__(self, rect: pygame.rect.Rect, background: pygame.surface.Surface, springConstant) -> None:
        super().__init__(rect, background)
        self.initMechanics(Kilogram(0))
        self.springConstant = springConstant
        self.length = rect.h

    def extend(self, displacement: vec2d):
        from pygame.transform import scale
        newSize = vec2d(self.image.get_size()) + displacement
        if newSize.dot(vec2d(0, -1)) >= 0: return
        self.image = scale(self.image, newSize)
        newRect = self.image.get_rect()
        newRect.topleft = self.rect.topleft
        self.rect = newRect

    # override
    def move(self, offset: vec2d):
        self.extend(offset)

    # override
    def tickMechanics(self):
        from ..utils import ClockLoader
        springForce = vec2d(0, 1) * self.springConstant * (self.length - self.rect.h) * ClockLoader.getTime()
        print(self.length - self.rect.h)
        self.appliedForces.append(springForce)
        
        force = self.calcAppliedForce()
        x = force / (self.springConstant)
        self.extend(x)

    def update(self) -> None:
        self.tickMechanics()
