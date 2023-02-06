from ..interface import Mechanics
from ...utils import Kilogram, vec2d
from . import ParticleGroup
from typing import Optional

class Particle(Mechanics):

    _group: Optional[ParticleGroup] = None
    _pos: vec2d

    def __init__(self, mass: Kilogram, pos: vec2d) -> None:
        self.initMechanics(mass)
        self.pos = pos

    # override
    def tickMechanics(self) -> None:
        displacement = super().tickMechanics()
        self.move(displacement, offset=True)

        if self.pos[1] > 720 and self.velocity.dot(vec2d(0, 1)) >= 0:
            self.velocity *= -1

    def move(self, pos: vec2d, offset=True) -> None:

        if not offset:
            pos -= self.pos

        if not self.group is None:
            self.group.move(pos)
            return 

        self.directMove(pos)

    def directMove(self, offset: vec2d) -> None:
        self.pos += offset

    def copy(self) -> 'Particle':
        from copy import copy
        return copy(self)

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
    