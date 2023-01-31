from .interface import Mechanics
from .baseObject import BaseObject
from pygame.rect import Rect
from pygame.surface import Surface
from ..utils import Kilogram, ConfigLoader, ClockLoader, vec2d
from typing import Self


class GravityObject(BaseObject, Mechanics):


    def __init__(self, rect: Rect, background: Surface, mass: Kilogram) -> None:
        super().__init__(rect, background)
        self.initMechanics(mass)

    @classmethod
    def fromObject(cls, obj: BaseObject, mass: Kilogram) -> Self:
        return cls(obj.rect, obj.image, mass)

    # Overriding
    def update(self) -> None:
        gravityConstant = ConfigLoader.gravityConstant
        clock = ClockLoader.clock
        
        gravity = vec2d(0, 1) * gravityConstant * clock.get_time() / 1000 # ms to sec
        self.accelerate += gravity
        displacement = self.tickMechanics()
        self.rect.move_ip(displacement)

        # this selection is for test purposes
        from pygame import mouse
        from pygame.display import get_window_size
        from pygame.rect import Rect

        screenRect = Rect(0, 0, *get_window_size())
        if not screenRect.contains(self.rect):
            self.rect.clamp_ip(screenRect)

        if mouse.get_pressed()[0]:
            self.accelerate = vec2d()
            self.velocity = vec2d()
            self.rect.update(*mouse.get_pos(), self.rect.width, self.rect.height)

