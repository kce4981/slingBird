from ...utils import Kilogram, vec2d

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # TYPE_CHECKING will be false on runtime, which resolves circular import error
    from . import Particle


class ParticleGroup:

    _particle: tuple['Particle']

    def __init__(self, particles: tuple['Particle']) -> None:

        self.particle = particles
        for p in particles:
            p.group = self
        
    
    def move(self, offset: vec2d):
        for p in self.particle:
            p.directMove(offset)

    @property
    def mass(self) -> Kilogram:
        massSum = Kilogram(0)
        for p in self.particle:
            massSum.value += p.mass.value

        return massSum

    @property
    def accelerate(self) -> vec2d:
        acc = vec2d()

        for p in self.particle:
            acc += p.accelerate
        
        return acc

    @property
    def velocity(self) -> vec2d:
        vel = vec2d()

        for p in self.particle:
            vel += p.velocity

        return vel

    @property
    def particle(self) -> tuple['Particle']:
        return self._particle

    @particle.setter
    def particle(self, value: tuple['Particle']) -> None:
        self._particle = value