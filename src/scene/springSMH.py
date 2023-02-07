from . import BaseScene
from ..objects import Spring, SingleParticle
from ..utils import vec2d


class SpringSMH(BaseScene):

    def __init__(self) -> None:
        super().__init__("Draggable")

        pos = vec2d(640, 300)

        self.singleParticle = SingleParticle(pos)
        self.spring = Spring(pos - vec2d(0, 100), self.singleParticle.mainParticle, 1.0, length=50)

        self.addGroup(self.singleParticle, self.spring)

        