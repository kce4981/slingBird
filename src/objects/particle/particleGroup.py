from ...utils import Kilogram, vec2d

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # TYPE_CHECKING will be false on runtime, which resolves circular import error
    from . import Particle


class ParticleGroup:

    particles: tuple['Particle']

    def __init__(self, particles: tuple) -> None:

        self.particles = particles
        for p in particles:
            p.group = self
        
    
    def move(self, offset: vec2d):
        for p in self.particles:
            p.directMove(offset)

    @property
    def mass(self) -> Kilogram:
        massSum = Kilogram(0)
        for p in self.particles:
            massSum.value += p.mass.value

        return massSum

    @property
    def accelerate(self) -> vec2d:
        acc = vec2d()

        for p in self.particles:
            acc += p.accelerate
        
        return acc

    @property
    def velocity(self) -> vec2d:
        vel = vec2d()

        for p in self.particles:
            vel += p.velocity

        return vel