from . import BaseScene
from ..objects import BaseObject, GravityObject
from ..utils import Kilogram
from pygame.surface import Surface
from pygame import sprite

class GravityTest(BaseScene):

    def __init__(self):

        super().__init__("Draggable")

        background = Surface((30, 30))
        background.fill((121, 204, 43))
        baseObject = BaseObject(background.get_rect(), background)

        mass = Kilogram(3)
        testGravity = GravityObject.fromObject(baseObject, mass)
        
        self.addGroup(testGravity)
