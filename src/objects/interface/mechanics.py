from typing import Protocol, Union
from abc import abstractmethod
from ...utils import Kilogram, vec2d, Face


class Mechanics(Protocol):

    mass: Kilogram
    velocity: vec2d
    _accelerate: vec2d
    _appliedForces: list[vec2d]
    connected: dict[Face, Union['Mechanics', None]]

    def initMechanics(self, mass: Kilogram) -> None:
        self.velocity = vec2d()
        self.accelerate = vec2d()
        self.mass = mass
        self.appliedForces = []
        self.connected = {f:None for f in Face}

    def connect(self, obj: 'Mechanics', face: Face):
        self.connected[face] = obj
        obj.connected[Face.getReverse(face)] = self

    def calcAppliedForce(self) -> vec2d:

        forceSum = vec2d()
        for force in self.appliedForces:
            forceSum += force

        self.appliedForces.clear()

        # I misunderstood how spring works
        # but i don't want make my 7 hours of work become nothing
        # so i'll just left it as is

        for face, connectedObj in self.connected.items():
            if connectedObj is None: continue
            if forceSum.dot(face.value) == 0: continue
            
            projForce = forceSum.project(face.value)
            connectedObj.appliedForces.append(projForce)

        # print(f'{self.__class__.__name__} {forceSum}')
        return forceSum

    def tickMechanics(self):

        force = self.calcAppliedForce()
        self.accelerate += force / self.mass.getValue()
        self.velocity += self.accelerate
        
        for face, connectedObj in self.connected.items():
            if not connectedObj: continue
            connectedObj.move(self.velocity)


        self.move(self.velocity)

    @property
    def accelerate(self) -> vec2d:
        return self._accelerate

    @accelerate.setter
    def accelerate(self, value: vec2d) -> None:
        self._accelerate = value

    @property
    def appliedForces(self) -> list[vec2d]:
        return self._appliedForces

    @appliedForces.setter
    def appliedForces(self, value: list[vec2d]) -> None:
        self._appliedForces = value

    # Shadowing BaseObject.move
    @abstractmethod
    def move(self, offset: vec2d):
        raise NotImplementedError
