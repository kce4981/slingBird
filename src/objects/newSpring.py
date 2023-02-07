from . import BaseObject, MechObject
from .interface import Mechanics
from ..utils import vec2d


class Spring(MechObject):

    initLength: float
    length: float

    def __init__(self, obj1: MechObject, obj2: MechObject) -> None:

        self.initLength = (vec2d(obj1.rect.topleft) - vec2d(obj2.rect.bottomleft)).length()
        self.length = self.initLength

    