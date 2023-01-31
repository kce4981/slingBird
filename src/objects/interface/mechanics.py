from typing import Protocol
from abc import abstractmethod
from ...utils.math import vec2d
from ...utils.unit import Kilogram

class Mechanics(Protocol):

    mass: Kilogram
    velocity: vec2d
    accelerate: vec2d
    appliedForces: list[vec2d]

    def initMechanics(self, mass: Kilogram) -> None:
        self.velocity = vec2d()
        self.accelerate = vec2d()
        self.mass = mass
        self.appliedForces = []

    def calcAppliedForce(self) -> vec2d:
        forceSum = vec2d()
        for force in self.appliedForces:
            forceSum += force

        self.appliedForces.clear()
        return forceSum

    def tickMechanics(self) -> vec2d:

        force = self.calcAppliedForce()
        self.accelerate += force / self.mass.getValue()
        self.velocity += self.accelerate
        return self.velocity
