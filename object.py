from utils.math import vec2d
import utils.unit as unit


class object:

    appliedForce = []

    def __init__(self, mass: unit.kilogram, pos: vec2d) -> None:
        self.mass = mass
        self.pos = pos

    def calculate_Force(self) -> vec2d:

        force = vec2d(0, 0)

        for f in self.appliedForce:
            force += f

        return force

    def tick(self) -> None:

        self.calculate_Force()
