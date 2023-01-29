from ..utils.math import vec2d
from ..utils import unit
from pygame.sprite import Sprite
import pygame


class BaseObject(Sprite):

    appliedForce: list[vec2d]
    velocity: vec2d
    rect: pygame.rect.Rect
    screenRect: pygame.rect.Rect

    def __init__(self, mass: unit.kilogram, rect: pygame.rect.Rect, img: pygame.surface.Surface, screenRect=None) -> None:
        self.mass = mass
        self.appliedForce = []
        self.velocity = vec2d()

        if screenRect is None:
            self.screenRect = pygame.display.get_surface().get_rect()
        else:
            self.screenRect = screenRect

        self.rect = rect
        self.image = img
        Sprite.__init__(self)

    def calculate_Force(self) -> vec2d:
        force = vec2d(0, 0)
        for f in self.appliedForce:
            force += f

        self.appliedForce.clear()
        return force

    def move(self):
        newRect = self.rect.move(*self.velocity)
        if not self.screenRect.contains(newRect):
            newRect = newRect.clamp(self.screenRect)

        self.rect = newRect

    def update(self):
        
        force = self.calculate_Force()
        self.velocity += force / self.mass.getValue()
        self.move()
        print(self.velocity)