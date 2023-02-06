from ..interface import Mechanics
from ...utils import Kilogram, vec2d
from . import ParticleGroup

class Particle(Mechanics):

    _group: 'ParticleGroup'
    _pos: vec2d

    def __init__(self, mass: Kilogram, pos) -> None:
        self.initMechanics(mass)
        self.pos = pos


    @property
    def group(self) -> 'ParticleGroup':
        return self._group

    @group.setter
    def group(self, group):
        self._group = group

    @property
    def pos(self) -> vec2d:
        return self._pos

    @pos.setter
    def pos(self, newPos):
        self._pos = newPos
    