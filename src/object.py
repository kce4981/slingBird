from utils.math import vec2d
from utils import unit
from pygame.sprite import Sprite
import pygame


class object(Sprite):

    appliedForce: list[vec2d] = []
    velocity: vec2d = vec2d()

    def __init__(self, mass: unit.kilogram, pos: vec2d, rect: pygame.Rect) -> None:
        Sprite.__init__(self)
        self.mass = mass
        self.pos = pos
        self.rect = rect

    def calculate_Force(self) -> vec2d:
        force = vec2d(0, 0)
        for f in self.appliedForce:
            force += f

        self.appliedForce.clear()
        return force

    def update(self):
        
        force = self.calculate_Force()
        self.velocity += force
        self.pos += self.velocity
