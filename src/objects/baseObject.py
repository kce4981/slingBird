from ..utils.math import vec2d
from ..utils import unit
from pygame.sprite import Sprite
import pygame


class BaseObject(Sprite):

    appliedForce: list[vec2d]
    velocity: vec2d

    def __init__(self, mass: unit.kilogram, pos: vec2d, rect: pygame.Rect, img: pygame.Surface) -> None:
        self.mass = mass
        self.pos = pos
        self.appliedForce = []
        self.velocity = vec2d()

        self.rect = rect
        self.image = img
        Sprite.__init__(self)

    def calculate_Force(self) -> vec2d:
        force = vec2d(0, 0)
        for f in self.appliedForce:
            force += f

        self.appliedForce.clear()
        return force

    def update(self):
        
        force = self.calculate_Force()
        self.velocity += force / self.mass.getValue()
        self.pos += self.velocity
        self.rect = self.rect.move(self.velocity)
